class Person():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class Student(Person):
    def __init__(self, student_id, firstName, lastName):
        self.student_id = student_id
        super().__init__(firstName, lastName)
        self.exams = []

    def addExam(self,courseName,grade):
        #each exam is a tuple organized as follows: (nameOfCourse, grade)
        exam = (courseName, grade)
        self.exams.append(exam)

    def getAllExams(self):
        #lists are mutable objects, which might prove problematic
        #if we return the list itself
        #instead, we will construct a new list, passing the exams list as a parameter
        #the list constructor constructs a new list and returns a copy of the exams list
        return list(self.exams)

    def getExamCount(self):
        return len(self.exams)

    def getExamAverageGrade(self):
        total = 0
        if (len(self.exams) == 0):
            return None
        else:   
            for currentExam in self.exams:
                total += float(currentExam[1])
            return (total/len(self.exams))

            #another way of doing the above
            #for name,grade in self.exams:
                #sum += grade
            #return sum/n


#error handling, is thrown when a student is searched for but doesn't
#exist
class StudentDoesNotExistException(Exception):
    pass

class University():
    def __init__(self):
        #instantiates a dictionary where keys are
        #student IDs and values are student objects
        self.students = {}

    #adds a student to the university
    #a student object is passed as a parameter to the function
    def addStudent(self,s):
        studentID = s.student_id
        #adds student to student dictionary using the student ID as the key
        self.students[studentID] = s

    def getStudentByID(self,studentID):
        try:
            #returns student by ID
            s = self.students[studentID] 
            return s
        except KeyError:
            raise StudentDoesNotExistException(studentID) from None
            
    
    def loadStudents(self, fileName):
        #open file in read-only mode
        f = open(fileName, "r")

        for line in f:
            line = line.strip()
            #split each line of the CSV file by a comma to read in the information of each field
            studentID,lastName,firstName = line.split(",")
            s = Student(studentID,firstName,lastName)
            self.addStudent(s)
        f.close()

    def loadExams(self, fileName):
        #open file in read-only mode
        #having the file opened in read-only mode is the default
        #f = open(filename) is one way to do this
        f = open(fileName, "r")

        for line in f:
            line = line.strip()
            studentID,courseName,grade = line.split(",")
            exam = (courseName,grade)
            self.students[studentID].exams.append(exam)

        f.close()

    #return a report of all the students, the number of exams they have passed
    #and their average grade across all exams taken
    def generateStudentReport(self):
        #declare an empty list that will hold the output
        output = []

        for studentID in self.students:
            #assign student object to currentStudent variable
            currentStudent = self.students[studentID]
            #built the desired informational tuple for the current student
            infoTuple = (currentStudent.student_id, currentStudent.lastName, currentStudent.firstName,currentStudent.getExamCount(),currentStudent.getExamAverageGrade())
            #append the tuple to the output list
            output.append(infoTuple)
        #return the set of information, which is stored in the output list
        return output

    def getStudentsByLastName(self, lastName):
        output = []

        for studentID in self.students:
            #if the last name of the current student matches the one we're looking for
            if (self.students[studentID].lastName.lower()) == lastName.lower():
                #add the student to the output list
                output.append(self.students[studentID])
        #return the list of students whose last names match the one we're searching for
        return output

    def saveStudents(self, fileName):
        f = open(fileName, "w")

        for currentKey in self.students:
            stud = self.students[currentKey]
            studentID = stud.student_id
            firstName = stud.firstName
            lastName = stud.lastName

            f.write(studentID + "," + lastName + "," + firstName +"\n") 
        f.close()
        
    def saveExams(self, fileName):
        f = open(fileName, "w")

        for currentKey in self.students:
            stud = self.students[currentKey]

            #print(stud.exams)
            for currentExam in stud.exams:
                nameOfCourse = str(currentExam[0])
                gradeOfExam = str(currentExam[1])
                f.write(stud.student_id + "," + nameOfCourse + "," + gradeOfExam + "," + "\n") 
        f.close()

#Testing the person class, step #1
#n = Person("jodjo","poekrpe")
#print(n.firstName)
#print(n.lastName)

#Testing the Person and Student classes, step #2
#john = Student("0123", "John","Smith")
#print(john.lastName)
#print(john.student_id)
#print(john.getAllExams())
#print(john.getExamAverageGrade())

#john.addExam("Programming",30)
#john.addExam("Algorithms",28)

#print(john.getAllExams())
#print(john.getExamAverageGrade())

#Testing the initial methods of the University class, step #3
#mary = Student("0111", "Mary","Smith")
#john = Student("0222", "John","Smith")

#u = University()
#u.addStudent(john)
#u.addStudent(mary)

#s = u.getStudentByID("0111")
#print(s.firstName)
#t = u.getStudentByID("0222")
#print(t.firstName)

#Testing the loadStudents() function from the University class, step #4
#u = University()
#u.loadStudents('students.csv')
#bill = u.getStudentByID("0333")
#print(bill.lastName)

#Testing the loadExams() and generateStudentReport() functions from the University class, steps #5, 6, & 7
#u = University()
#u.loadStudents('students.csv')
#u.loadExams('exams.csv')
#bill = u.getStudentByID('0333')
#print(bill.getExamAverageGrade())
#print(u.generateStudentReport())
#print(u.getStudentsByLastName("smith"))

#Testing the saveStudents() and saveExams() functions from the University class, step #8

#u = University()
#u.loadStudents('students.csv')
#u.loadExams('exams.csv')
#u.saveStudents("savedStudents.csv")
#u.saveExams("savedExams.csv")

