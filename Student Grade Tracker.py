class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # 'lecturer' or 'student'

# Function to calculate the letter grade based on the  score
def calculate_letter_grade(score):
    if 85 <= score <= 100:
        return 'A+'
    elif 80 <= score <= 84:
        return 'A'
    elif 75 <= score <= 79:
        return 'B+'
    elif 70 <= score <= 74:
        return 'B'
    elif 65 <= score <= 69:
        return 'C+'
    elif 60 <= score <= 64:
        return 'C'
    elif 55 <= score <= 59:
        return 'D+'
    elif 50 <= score <= 54:
        return 'D'
    else:
        return 'E'

# Function to create a new user account
def create_account(users):
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    role = input("Are you a lecturer or a student? (Enter 'lecturer' or 'student'): ").lower()
    if role not in ['lecturer', 'student']:
        print("Invalid role. Account creation failed.")
        return
    users[username] = User(username, password, role)
    print(f"Account created successfully for {role} '{username}'.")

# Function to login a user
def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username].password == password:
        print(f"Login successful. Welcome, {users[username].role} '{username}'!")
        return users[username]
    else:
        print("Login failed. Invalid username or password.")
        return None

# Function to input grades and names (only available to lecturers)
def input_grades(courses, num_students):
    student_grades = {}  # Initialize an empty dictionary to store grades
    student_names = []  # List to store student names

    # Loop through each student to input names and scores
    for i in range(num_students):
        name = input(f"Enter name for Student {i + 1}: ").strip().lower()  # Normalize the student name
        student_names.append(name)
        student_grades[name] = {}  # Initialize a nested dictionary for each student
        print(f"\nEntering grades for {name}:")
        for course in courses:
            score = float(input(f"Enter score for {course}: "))
            student_grades[name][course] = score
    return student_grades, student_names

# Function to calculate the average score for each course
def calculate_course_averages(student_grades, num_students):
    course_averages = {}
    for course in student_grades[next(iter(student_grades))]:  # Get the first student's courses
        total_score = sum(student_grades[student][course] for student in student_grades)
        course_average = total_score / num_students
        course_averages[course] = course_average
        # Print the average for the current course
        print(f"Average for {course}: {course_average:.2f}")
    return course_averages

# Function to display the results, including individual grades and course averages
def display_results(student_grades, course_averages, student_names):
    # Display individual grades for each student
    for name in student_names:
        print(f"\nGrades for {name}:")
        for course in student_grades[name]:
            score = student_grades[name][course]
            letter_grade = calculate_letter_grade(score)
            print(f"{course}: {score} - {letter_grade}")

    # Display average grades for each course
    print("\nCourse Averages:")
    for course, average in course_averages.items():
        average_letter_grade = calculate_letter_grade(average)
        print(f"{course}: {average:.2f} - {average_letter_grade}")

# Function to post grades (only available to lecturers)
def post_grades(courses, student_grades, posted_grades, student_names):
    print("Posting grades for all students...")
    for name in student_names:
        for course in courses:
            if course not in posted_grades:
                posted_grades[course] = {}
            posted_grades[course][name] = student_grades[name][course]
    print("Grades posted successfully.")

# Function for students to view their posted grades and course averages
def view_posted_grades(student_name, posted_grades, course_averages):
    student_name = student_name.strip().lower()  # Normalize the student name
    print(f"Grades for {student_name}:")
    for course, grades in posted_grades.items():
        if student_name in grades:
            score = grades[student_name]
            letter_grade = calculate_letter_grade(score)
            average = course_averages[course]
            average_letter_grade = calculate_letter_grade(average)
            print(f"{course}: {score} - {letter_grade} (Course Average: {average} - {average_letter_grade})")
        else:
            print(f"{course}: No grade posted yet.")

# Main function to run the program
def main():
    users = {}  # Dictionary to store user accounts
    posted_grades = {}  # Dictionary to store posted grades
    course_averages = {}  # Dictionary to store course averages
    while True:
        print("\nWelcome to the Student Grade Tracker")
        print("1. Create a new account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            create_account(users)
        elif choice == '2':
            user = login(users)
            if user is not None and user.role == 'lecturer':
                # List of courses
                courses = ["Written and Oral Communication", "Introduction to Computing and Information Systems",
                           "Foundations of Design and Entrepreneurship", "Calculus I"]
                # Input the number of students
                num_students = int(input("Enter the number of students: "))

                # Input names and grades for each student
                student_grades, student_names = input_grades(courses, num_students)
                # Calculate course averages
                course_averages = calculate_course_averages(student_grades, num_students)
                # Display the results
                
                display_results(student_grades, course_averages, student_names)
                # Post grades
                post_grades(courses, student_grades, posted_grades, student_names)
            elif user is not None and user.role == 'student':
                student_name = input("Enter your name: ")
                view_posted_grades(student_name, posted_grades, course_averages)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
 