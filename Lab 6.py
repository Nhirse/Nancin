import pickle

class CourseGrades:
    def __init__(self):
        self.course_name=""
        self.stu_id=[]
        self.stu_grades=[]

    def get_details(self):
        self.course_name=input("Enter the name of the course: ")
        for i in range(1,6):
            self.stu_id.append(input(f"Enter Student {i}'s ID: "))
            self.stu_grades.append(input(f"Enter Student {i}'s grade: "))

# for i in range(0,4):
s1=CourseGrades()
s1.get_details()
f = open('myCourseGrades.dat', 'ab')
pickle.dump(s1,f)
f.close()

f = open('myCourseGrades.dat', 'rb')
while 1:
    try:
        data=pickle.load(f)
        print(data.course_name)
        print(data.stu_id)
        print(data.stu_grades)
    except EOFError:
        break
f.close()




