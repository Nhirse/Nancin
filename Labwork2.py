myStudents={"Student 1":
                {"Name":"Nancin",
                "Lab 1":34,
                "Lab 2":56,
                "Lab 3":54,
                "Lab 4":54,
                "Lab 5":26,
                "Total":39,
                "Percent":69.56,
                "Average":29.45}
            }
x=1

while 1:
    print("1. Add a student")
    print("2. Delete a student")
    print("3. Modify a student")
    print("4. Display all students")
    print("5. Exit the menu")
    choice=int(input("Welcome to the student grade book! Choose a number from the menu for what you'd like to do: "))
    if choice==5:
        print("You've exited the program. Farewell!")
        break
    elif choice==1:
        name=input("Type the name of the student whose grades you're entering: ")
        lab1=int(input("Type this students lab 1 score: "))
        lab2 = int(input("Type this students lab 2 score: "))
        lab3 = int(input("Type this students lab 3 score: "))
        lab4 = int(input("Type this students lab 4 score: "))
        lab5 = int(input("Type this students lab 5 score: "))
        if type(name)==str:
            x+=1
            total=lab1+lab2+lab3+lab4+lab5
            if total<=250:
                percentage=round((total/250)*100,2)
                average=round(total/5,2)

                myStudents.update({f"Student {x}":
                                       {"Name":name,
                                        "Lab 1":lab1,
                                        "Lab 2":lab2,
                                        "Lab 3":lab3,
                                        "Lab 4":lab4,
                                        "Lab 5":lab5,
                                        "Total":total,
                                        "Percentage":percentage,
                                        "Average":average}})
        else:
            print("Invalid Input. Remember, Lab scores should be out of 50. Try again.")
    elif choice==2:
        name = input("Which student do you want to remove? ")
        if type(name)==str:
            checkName=True
            for i in myStudents.copy():
                if i==name:
                    checkName=False
                    del myStudents[i]
                    x-=1
            if checkName:
                print("The Student chosen isn't in the list. Make sure you write Student and their number. Not their name. Try again")
    elif choice==3:
        title=input("Type the student title you want to modify (in the form Student 1, Student 2 etc): ")
        doc=input("Type the document you want to change (Name, Lab 1, Lab 2 etc): ")
        if type(title) == str and type(doc==str):
            if (doc == "Name"):
                value=input("Type what you want to change the value of the document to: ")
                myStudents[title][doc] = value
            elif doc==("Percentage" or "Average" or "Total"):
                print("Can't change these values. They will recalculate if you modify the labs.")
            elif type(myStudents[title][doc])==int:
                value=int(input("please input the points you want to change the lab to: "))
                if 0 <= value <= 50:
                    myStudents[title][doc] = value
                    total=myStudents[title]["Lab 1"]+myStudents[title]["Lab 2"]+myStudents[title]["Lab 3"]+myStudents[title]["Lab 4"]+myStudents[title]["Lab 5"]
                    percentage=round(total/250*100,2)
                    average=round(total/5,2)
                    myStudents[title]["Total"] = total
                    myStudents[title]["Percent"] = percentage
                    myStudents[title]["Average"]= average
                else:
                    print("Points can't be greater than 50 nor less than 0. Try again.")
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Try again.")
    elif choice==4:
        print(myStudents)
    else:
        print("Invalid Input.Try again.")

