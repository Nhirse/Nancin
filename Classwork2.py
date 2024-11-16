NameList=[]
AgeList=[]
check=False
while 1:
    print("1. Add")
    print("2. Remove")
    print("3. Replace")
    print("4. Display")
    print("5. Exit")
    print("Hi! You can use this menu to build your name list and your age list.")
    x=int(input("Type the number from the menu of what you'd like to do: "))
    if x==5:
        print("You chose to exit the menu. Bye Bye!")
        break
    elif x==1:
        name=input("Please type the name of the person you want to add to your list: ")
        age=int(input("Please type the age of this person: "))
        if type(name)==str and name not in NameList and age not in AgeList:
            NameList.append(name)
            AgeList.append(age)
            print(" ")
        else:
            print("Invalid input. Make sure the name you're entering isn't already there. Please try again.\n")
    elif x==2:
        name=input("Please type the name of the person you want to remove from your list: ")
        age=int(input("Please type the age of this person: "))
        if name in NameList and age in AgeList:
            for i in range(0,len(NameList)-1):
                if NameList[i]==name:
                    NameList.remove(name)
            for j in range(0,len(AgeList)-1):
                if AgeList[j]==age:
                    AgeList.remove(age)
            print(" ")
        else:
            print("Either the name or the age selected are not found in the lists. Please try again.\n")
    elif x==3:
        name=input("Choose a replacement name: ")
        replace=input("Choose the previous name which you want replaced: ")
        age=int(input("Choose the replacement age for this person: "))
        replaceAge=int(input("Choose the previous age which you want replaced: "))
        if replace in NameList and replaceAge in AgeList:
            for i in range(0,len(NameList)):
                if NameList[i]==replace:
                    NameList[i]=name
            for j in range(0, len(AgeList)):
                if AgeList[j]==replaceAge:
                    AgeList[j] = age
        else:
            print("Either the name or the age you want replaced isn't in the List. Try again")
    elif x==4:
        print(NameList)
        print(AgeList)
    else:
        print("Invalid input. Please choose option from menu.")