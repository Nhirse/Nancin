class Person:
    def __init__(self, nn, dd, gg): #__init__ allows this constructor to be implicitly called whenever an instance of the class is created.
        self.__pname=nn
        self.__dob=dd
        self.__gender=gg

    def display(self):
        print("Person_Name: ", self.__pname)
        print("Person_DOB: ", self.__dob)
        print("Person_Gender: ", self.__gender)

class Student(Person): #
    def __init__(self, x, y,z,a,b):
        Person.__init__(self, x,y,z) #automatically constructing the Person along with it's three variables, now given to x y z, into Student class
        self.major=a
        self.id=b

class Faculty(Person):
    def __init__(self, x,y,z,a,b):
        Person.__init__(self,x,y,z)
        self.dept=a
        self.id=b

s=Student("Nancin","11/18","Female","Computer Science",1079649)
print(s.display())
