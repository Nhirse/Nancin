class Student:
    def __init__(self):
        self.sid=""
        self.stuname=""
        self.major=""
        self.advisor=" "

    def create_student(self):
        self.sid = input("Enter Student id: ")
        self.stuname= input("Enter Student Name: ")
        self.major=input("Enter Student Major: ")

    def display(self):
        print("Student id: "+self.sid)
        print("Student Name: "+self.stuname)
        print("Student Major: "+self.major)
        print("Student Advisor: "+Student.assign_advisor(self))

    def update(self):
        while 1:
            print("1. Change id")
            print("2. Change major")
            print("3. Back to main menu")
            choose=int(input("Type the number from the menu of what you'd like to change: "))
            if choose==3:
                break
            elif choose==1:
                self.sid=input("Enter what you want to change the student id to: ")
            elif choose==2:
                self.major=input("Enter what you want to change the student major to: ")
            else:
                print("invalid input. Please try again.")
            Student.display(self)

    def assign_advisor(self):
        self.advisor=myFaculties[0].name
        return self.advisor

class Faculty:
    def __init__(self):
        self.id=""
        self.name=""
        self.dept=""
        self.salary=""

    def create_faculty(self):
        self.id=input("Enter Faculty id: ")
        self.name=input("Enter Faculty name: ")
        self.dept=input("Enter Faculty department: ")
        self.salary=input("Enter Faculty salary: ")

    def display(self):
        print("Faculty id: "+self.id)
        print("Faculty name: " + self.name)
        print("Faculty department: " + self.dept)
        print("Faculty salary: " + self.salary)

    def update(self):
        while 1:
            print("1. Change id")
            print("2. Change department")
            print("3. Change salary")
            print("4. Back to main menu")
            choose = int(input("Type the number from the menu of what you'd like to change: "))
            if choose == 4:
                print("Once again, select an option from the main menu: ")
                break
            elif choose == 1:
                self.id = input("Enter what you want to change the faculty id to: ")
            elif choose==2:
                self.dept = input("Enter what you want to change the faculty department to: ")
            elif choose==3:
                self.salary = input("Enter what you want to change the faculty salary to: ")
            else:
                print("invalid input. Please try again.")
            Faculty.display(self)


class Department:
    def __innit__(self):
        self.id=""
        self.name = ""
        self.building = " "
        self.budget = " "
        self.list_of_faculty = " "

    def create_department(self):
        self.id =input("Enter department id: ")
        self.name =input("Enter department name: ")
        self.building = input("Enter department building: ")
        self.budget = input("Enter department budget: ")
        self.list_of_faculty = input("Enter names of faculty in department: ")

    def display(self):
        print(self.id)
        print(self.name)
        print(self.building)
        print(self.budget)
        print(self.list_of_faculty)



    def update(self):
        while 1:
            print("1. Change budget")
            print("2. Change building")
            print("3. Change list of faculty")
            print("4. Back to main menu")
            choose = int(input("Type the number from the menu of what you'd like to change: "))
            if choose == 4:
                break
            elif choose == 1:
                self.budget = input("Enter what you want to change the department budget to: ")
            elif choose == 2:
                self.building = input("Enter what you want to change the department building to: ")
            elif choose == 3:
                self.list_of_faculty = input("Enter what you want to change the list of faculty to: ")
            else:
                print("invalid input. Please try again.")
            Department.display(self)

class Course:
    def __init__(self):
        self.course_no=""
        self.course_name=""
        self.dept_name=""
        self.credits=""

    def create_course(self):
        self.course_no = input("Enter the course number: ")
        self.course_name = input("Enter the course name: ")
        self.dept_name = input("Enter the department name: ")
        self.credits = input("Enter the course credits: ")

    def display_course(self):
        print(self.course_no)
        print(self.course_name)
        print(self.dept_name)
        print(self.credits)

    def update_course(self):
        while 1:
            print("1. Change department of course")
            print("2. Change course credits")
            print("3. Back to main menu")
            choose=int(input("Type the number from the menu of what you'd like to change: "))
            if choose==3:
                break
            elif choose==1:
                self.dept_name= input("Enter what you want to change the department of the course to: ")
            elif choose==2:
                self.credits= input("Enter what you want to change the course credits to: ")
            else:
                print("invalid input. Please try again.")
        Course.display_course(self)

myStudents=[]
myFaculties=[]
myDepartments=[]
myCourses=[]


while 1:
    print("1. Create a Student")
    print("2. Display a Student")
    print("3. Edit a Student")
    # print("3.5. Assign a Faculty")
    print("4. Create a Faculty")
    print("5. Display a Faculty")
    print("6. Edit a Faculty")
    print("7. Create a Department")
    print("8. Display a Department")
    print("9. Edit a Department")
    print("10. Create a Course")
    print("11. Display a Course")
    print("12. Edit a Course")
    print("99. Exit Program")
    choice=int((input("Please select from the menu what you'd like to do by typing the corresponding number: ")))
    if choice==99:
        print("You've exited the program. Farewell!")
        break
    elif choice==1:
        s=Student()
        s.create_student()
        myStudents.append(s)
    elif choice==2:
        dis=input("Type the id of the student you want to display: ")
        check=True
        for i in range(0,len(myStudents)):
            if myStudents[i].sid==dis:
                check =False
                myStudents[i].display()
            if check:
                print("Student could not be found. Please type another id.")
    elif choice==3:
        upd = input("Type the id of the student you want to update: ")
        check = True
        for i in range(0, len(myStudents)):
            if myStudents[i].sid == upd:
                check = False
                myStudents[i].update()
            if check:
                print("Student could not be found. Please type another id.")

    elif choice==4:
        f = Faculty()
        f.create_faculty()
        myFaculties.append(f)
    elif choice == 5:
        dis = input("Type the id of the Faculty you want to display: ")
        check = True
        for i in range(0, len(myFaculties)):
            if myFaculties[i].id == dis:
                check = False
                myFaculties[i].display()
            if check:
                print("Faculty could not be found. Please type another id.")
    elif choice == 6:
        upd = input("Type the id of the Faculty you want to update: ")
        check = True
        for i in range(0, len(myFaculties)):
            if myFaculties[i].id == upd:
                check = False
                myFaculties[i].update()
            if check:
                print("Faculty could not be found. Please type another id.")

    elif choice == 7:
        d=Department()
        d.create_department()
        myDepartments.append(d)
    elif choice == 8:
        dis = input("Type the id of the Department you want to display: ")
        check = True
        for i in range(0, len(myDepartments)):
            if myDepartments[i].id == dis:
                check = False
                myDepartments[i].display()
            if check:
                print("Department could not be found. Please type another id.")
    elif choice ==9:
        upd = input("Type the id of the Department you want to update: ")
        check = True
        for i in range(0, len(myDepartments)):
            if myDepartments[i].id == upd:
                check = False
                myDepartments[i].update()
            if check:
                print("Department could not be found. Please type another id.")

    elif choice == 10:
        c = Course()
        c.create_course()
        myCourses.append(c)
    elif choice == 11:
        dis = input("Type the id of the Course you want to display: ")
        check = True
        for i in range(0, len(myCourses)):
            if myCourses[i].course_no == dis:
                check = False
                myCourses[i].display_course()
            if check:
                print("Course could not be found. Please type another course number.")
    elif choice == 12:
        upd = input("Type the course number of the Course you want to update: ")
        check = True
        for i in range(0, len(myCourses)):
            if myCourses[i].course_no == upd:
                check = False
                myCourses[i].update_course()
            if check:
                print("Course could not be found. Please type another course number.")






