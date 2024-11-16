

dict = {
        }
x=0
y=0
def Enqueue():
    name=input("What's the name of the book you'd like to add? ")
    id = input("What's the id of this book? ")
    author = input("Whose the author of this book? ")
    edition = input("What's the edition of this book? ")
    publisher = input("Who's the publisher of this book? ")
    pub_year = int(input("What year was it published? "))
    globals()["x"]+=1
    dict.update({f"book{x}":
                           {"bookid": id,
                            "bookname": name,
                            "author": author,
                            "edition": edition,
                            "publisher": publisher,
                            "year of publishing": pub_year,}
                 })
    return 0

def Dequeue():
    dict.pop(f"book{1+y}")
    globals()["y"]+=1
    return 0

def Modify():
    book=input("Please type the name of the book you want to modify: ")
    doc=input("Please type what aspect of the book you want to modify. Example: author, publisher (all lower case): ")
    mod=input("Please type what you want to change this aspect to: ")
    if (type(book) and type(doc) and type(mod))==str:
        checkname=True
        for i in dict.copy():
            if dict.copy()[i]["bookname"]==book:
                checkname=False
                dict[i][doc]=mod
            else:
                print("Wrong input. Please try again. Check spelling and caps.")
    else:
        print("Wrong input. Please try again.")

def Search():
    search=input("Type id of the book you're looking for: ")
    if(type(search)==str):
        checkid=True
        for i in dict.copy():
            if dict.copy()[i]["bookid"]==search:
                checkid=False
                print(dict[i])
            else:
                print("Book not found.")
    else:
        print("invalid id. Try again.")


def Display():
    print(dict)

while 1:
    print("1. Add a book")
    print("2. Delete a book")
    print("3. Modify a book")
    print("4. Display all books")
    print("5. Search for a book")
    print("6. Exit the menu")
    select = int(input("Welcome. Choose the number for what you'd like to do: "))
    if select == 6:
        print("You are Exiting the Menu. Farewell.")
        break
    elif select == 1:
        Enqueue()
    elif select == 2:
        Dequeue()
    elif select == 3:
        Modify()
    elif select==4:
        Display()
    elif select==5:
        Search()