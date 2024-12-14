from FlashCards import Flash
#do textfile thing
#what if they type the same name for the flashcard

FlashCards=[]
FlashTitles=[]

def create_flash():
    title = input("Please type the title of your set of flashcards: ")
    f = Flash(title)  # Creates a new set of Flashcards, f
    FlashCards.append(f)  # add new flashcard set to a list of all the flashcard sets
    FlashTitles.append(f.getTitle())  # add the name of the flashcard set to list of all names of sets (Not necessarily necessary)
    access_flash(f)

def access_flash(z):
    print(f"This is your set of {z.getTitle()} flashcards")
    while 1:
        print("1. Add a Card")
        print("2. Delete a Card")
        print("3. Modify a Card")
        print("4. Display all cards")
        print("5. Take quiz on flashcards")
        print("6. Exit")
        select = int(input("Please type the number in the menu of what you want to do: "))
        if select==6:
            break
        elif select == 1:
            z.add_card() #add_card method should add a term and definition to two separate lists and the dictionary containing all flashcard information.
            #if else conditions check passed.
        elif select == 2:
            z.delete_card()
            # if else conditions check passed.
        elif select == 3:
            z.modify_card()
            # if else conditions check passed.
        elif select == 4:
            z.display_flash()
        else:
            print("Invalid input. Choose a number from the menu.")

def delete_flash():
    check=True
    sure=""
    while check or (sure=="nvm"):
        delete=input("Type the title of the Flashcard set you want to delete: ")
        for i in range(0,len(FlashTitles)):
            if delete==FlashTitles[i]:
                check=False
                FlashCards.pop(i)
                FlashTitles.pop(i)
        if(check):
            print("Couldn't find Flashcard set. Try again. ")
            sure=input("If you don't want to delete anything type nvm. If you do press enter.")

while 1:
    print("1. Create a new set of Flash Cards")
    print("2. Access previous Flash Cards")
    print("3. Delete a set of Flash Cards")
    print("4. Display all Flash Cards")
    print("5. Get quizzed on a set of Flash Cards")
    print("99. Exit")
    choice=int(input("Please type the number of what you want to do: "))
    if choice==99:
        break
    elif choice==1:
        create_flash()

    elif choice==2:
        check=True
        while check: #type the title of the flashcard set you want then do access_flash
            for i in range(0,len(FlashTitles)):
                print(f"{i+1}. {FlashTitles[i]}")
            select=int(input("Type a number from the menu the title of the flashcard set you want to access: "))
            for i in range(0,len(FlashCards)):
                if i+1==select:
                    check=False
                    access_flash(FlashCards[i])
            if(check):
                print("The flashcard set selected couldn't be found. Try again.")

    elif choice==3:
        delete_flash()

    elif choice==4:
        for i in range(0,len(FlashCards)):
            print(f"--{FlashTitles[i]}--")
            FlashCards[i].display_flash()
            print("\n")

    elif choice==5:
        check=True
        while check:
            for i in range(0, len(FlashTitles)):
                print(f"{i + 1}. {FlashTitles[i]}")
            select = int(input("Type a number from the menu the title of the flashcard set you want to be quizzed on: "))
            for i in range(0,len(FlashCards)):
                if i+1==select:
                    check=False
                    FlashCards[i].quiz()
            if(check):
                print("Couldn't find flashcard set. Try again.")

    else:
        print("Invalid input. Choose a number from the menu.")




