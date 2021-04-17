from university import Student, University, StudentDoesNotExistException

def main_menu():
    u = University()

    menu_str = """
        Please select an operation:
        
        1. Load students from CSV
        2. Load exams from CSV
        3. Save students to CSV
        4. Save exams to CSV
        5. Add a student
        6. Add an exam
        7. Show student data by student id
        8. Search students by last name
        9. Report students stats
        0. Exit

    """
    print("Welcome to our University Information System!")

    while True:
        print(menu_str)

        choice = input("Your choice:> ")

        if choice == '1':
            filename = input("Students CSV file name:> ")
            u.loadStudents(filename)
            print("Students loaded successfully.")
        if choice == '2':
            filename = input("Exams CSV file name:> ")
            u.loadExams(filename)
            print("Exams loaded successfully.")
        if choice == '3':
            fileName = input("Desired file name to save students to:> ")
            u.saveStudents(fileName)
            print("Students saved successfully.")
        if choice == '4':
            fileName = input("Desired file name to save exams to:> ")
            u.saveExams(fileName)
            print("Exams saved successfully.")
        if choice == '5':
             ID = input("Enter the ID of the student:> ")
             firstName = input("Enter the first name of the student:> ")
             lastName = input("Enter the last name of the student:> ")

             s = Student(ID, firstName,lastName)
             u.addStudent(s)

             print("Student added successfully.")
        if choice == '6':
            ID = str(input("Please enter the ID of the student for whom you would like to add the exam:> "))
            courseName = input("Please enter the name of the course for which the exam was taken:> ")
            examGrade = int(input("Please enter the exam grade:> "))
            u.getStudentByID(ID).addExam(str(courseName),str(examGrade))

            print("Exam added successfully.")           
        if choice == '7':
            show_student_data_by_id(u)
        if choice == '8':
            lastName = input("Enter the last name of the student:> ")
            getStudentsByLName(u, lastName)
        if choice == '9':
            reportStudentStats(u)
        if choice == '0':
            print("Application successfully exited.")
            exit
        else:
            print("\nPlease enter a valid selection.")
            
def show_student_data_by_id(u):
    ID = input("\nPlease enter student ID:> ")
    s = u.getStudentByID(ID)
    print("Name: " + s.firstName)
    print("Last name: " + s.lastName)
    print("Student ID: " + s.student_id + "\n")

    for currentExam in s.exams:
        print("Exam, Grade: " + str(currentExam[0]) + ", " + str(currentExam[1]))

def getStudentsByLName(u, lastName):
    listOfStudents = u.getStudentsByLastName(lastName)

    print("\nList of students in the university with this last name: \n")
    for currentStudent in listOfStudents:
        print("ID: " + currentStudent.student_id + ", " + currentStudent.firstName + " " + currentStudent.lastName)

def reportStudentStats(u):
    listOfStudentData = u.generateStudentReport()
    
    for currentStudent in listOfStudentData:
        print("\nStudent ID: " + currentStudent[0])
        print("First name: " + currentStudent[2])
        print("Last name: " + currentStudent[1])
        print("Number of exams taken: " + str(currentStudent[3]))
        print("Exams Average: " + str(currentStudent[4]))
        

main_menu()       
