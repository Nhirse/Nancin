import json
class Flash: #Create a title
    def __init__(self, t): #a flashcard object contains multiple cards within a dictionary flash.
        self.__all_cards={}
        self.__title_of_flash=t #When I create each flash object, it gives all the titles of previous ones
        self.__definitions_list=[]
        self.__terms_list=[]
        self.__term=""
        self.__definitions=""
        self.__counter=0

    def getTitle(self):
        return self.__title_of_flash

    def add_card(self):
        self.__term = input("Please type the term: ")
        self.__definitions = input("Please type the definition: ")
        self.__terms_list.append(self.__term)
        self.__definitions_list.append(self.__definitions)
        self.__counter+=1
        self.__all_cards.update({f"Card {self.__counter}":
                                     {f"{self.__term}": f"{self.__definitions}"}
                                 })

    # def update(self): #run through the terms_list, find the one that relates to the dictionary,
    #     for i in len(self.__terms_list):
    #         if self.__all_cards[f"Card {self.__counter}"][i] == self.__terms_list[i]:
    #             self.__all_cards[f"Card {self.__counter}"][i][({f"{self.__terms_list[i]}]: f"{self.__definitions_list[i]}"})

    def delete_card(self):
        check = True
        sure=""
        while check or (sure=="nvm"): #when the name is found in the list, check should be false and the loop should stop
            delete = input("Please type the term of the card you want to delete: ")
            for i in range(0,len(self.__terms_list)):
                if self.__terms_list[i]==delete:
                    check =False
                    self.__terms_list.pop(i)
                    self.__definitions_list.pop(i)
                    self.__all_cards.pop(f"Card {i+1}")
                    self.__counter-=1
            if(check):
                print("The card couldn't be found. Try Again.")
                sure = input("If you don't want to delete anything type nvm. If you do press enter.")


    def modify_card(self):
        check=True
        while check:
            for i in range(0,len(self.__terms_list)):
                print(f"Term {i+1}. {self.__terms_list[i]}: {self.__definitions_list[i]}")
            #choice=int(input("Please Choose a number from the menu what you'd like to modify: "))
            ter=int(input("Please type the number of the term you want to modify: "))
            for j in range(0,len(self.__terms_list)):
                if ter-1==j:
                    check=False
                    while 1:
                        print("1. Modify name")
                        print("2. Modify Definition")
                        print("3. Exit")
                        select=int(input("Type the number from the menu of you want to do: "))
                        if select==1:
                            name2=input("Please type what you want to change the term name to: ")
                            self.__all_cards[f"Card {j+1}"].pop(self.__terms_list[j])
                            self.__all_cards[f"Card {j+1}"].update({name2:self.__definitions_list[j]})
                            self.__terms_list[j] = name2
                        elif select==2:
                            defin=input("Please type what you want to change the definition to: ")
                            self.__definitions_list[j]=defin
                            self.__all_cards[f"Card {j+1}"].update({self.__terms_list[j]:defin})
                        elif select==3:
                            break
                        else:
                            print("Invalid input. Try again.")
            if(check):
                print("Couldn't find card. Try again.")

    def display_flash(self):
        print(f"Title of Flashcard: {self.__title_of_flash}")
        print(self.__all_cards)

    def quiz(self):
        again="yes"
        while again=="yes":
            print(f"Welcome to the {self.__title_of_flash} quiz!") #Remember to ignore cases on all the input stuff
            print("You'll see a definition and try to type the correct term that matches it. Make sure the term you type is exact.\n")
            points=0
            #Consider using math.rand somehow
            for i in range(0,len(self.__definitions_list)):
                print(f"{i+1} {self.__definitions_list[i]}")
                answer=input("Term: ")
                if self.__terms_list[i]==answer:
                    print("Correct!\n")
                    points+=1
                else: #Would they want the correct answer?
                    print(f"Incorrect. The correct answer is {self.__terms_list[i]}\n")
            print(f"Your score out of {len(self.__terms_list)} is {points}.")
            print(f"Your quiz grade is {points/len(self.__terms_list)*100} percent.") #optional: saying good job, poor job, try again, or a letter grade
            again=input("If you would like to try again type the number yes. if not, type no to exit: ").lower()

    def to_dict(self): #stores the values of the current Flash object in a dictionary
        data = { "Title of flashcard":self.__title_of_flash,
                "All Cards":self.__all_cards,
                 "List of terms":self.__terms_list,
                 "List of definitions":self.__definitions_list,
        }
        return data

    # def to_object(self, data):  # parameter is a dictionary like that which to_dict creates
    #     obj = Flash(data["Title of flashcard"])
    #     obj.__all_cards = data["All Cards"]
    #     obj.__terms_list = data["List of terms"]
    #     obj.__definitions_list = data["List of definitions"]
    #     obj.__counter = len(obj.__terms_list)
    #     return obj























        
