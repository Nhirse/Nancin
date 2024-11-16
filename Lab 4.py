def remove():
    for i in myLendList:
        if i.lending_id==" ":
            myLendList.remove(i)

class Book:
    def __init__(self):
        self.title= " "
        self.book_id = " "
        self.author_id = " "
        self.edition_no = " "
        self.publisher = " "
        self.pub_year = " "

    def create_book(self):
        self.title = input("Enter the title of the book:")
        self.book_id = input("Enter the book id: ")
        self.edition_no = input("Enter the edition number: ")
        self.publisher = input("Enter the publisher: ")
        self.pub_year = input("Enter the year it was published: ")
        self.author_id = input("Enter the author's id: ")

    def display_book(self):
        print("Book id: "+self.book_id)
        print("Book title: " + self.title)
        print("author id: " + self.author_id)
        print("edition number " + self.edition_no)
        print("Publisher: " + self.publisher)
        print("Publishing year: " + self.pub_year)

class Author:
    def __init__(self):
        self.author_id= ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone_no = ""
        self.email_id = ""

    def create_author(self):
        self.author_id = input("Enter the author id: ")
        self.author_name = input("Enter the author name: ")
        self.affiliation = input("Enter the author affiliation: ")
        self.country = input("Enter the author's nationality: ")
        self.phone_no = input("Enter the author's phone number: ")
        self.email_id = input("Enter the author's email: ")

    def display(self):
        print("Author id: " + self.author_id)
        print("Author name: "+ self.author_name)
        print("Author affiliation: " + self.affiliation)
        print("Author nationality: " + self.country)
        print("Author phone number: " + self.phone_no)
        print("Author email: " + self.email_id)

class User:
    def __init__(self):
        self.user_id = ""
        self.username=""
        self.password=""
        self.address=""
        self.phone=""
        self.email_id=""

    def create_user(self):
        self.user_id=input("Enter the user id: ")
        self.username = input("Enter the user name: ")
        self.password=input("Enter the user password: ")
        self.address=input("Enter the user address: ")
        self.phone=input("Enter the user phone number: ")
        self.email_id=input("Enter the user's email: ")

    def display_user(self):
        print("User id: "+self.user_id)
        print("User Name: " + self.username)
        print("User password: " + self.password)
        print("User address: " + self.address)
        print("User phone number: " + self.phone)
        print("User Email: " + self.email_id)

class Lend_Book:
    def __init__(self):
        self.lending_id=" "
        self.book_id = " "
        self.user_id = " "
        self.lending_date = " "
        self.return_date =" "

    def create_lend(self):
        self.lending_id=input("Enter the lending id: ")
        lendbook=input("Type the name of the book to be lent: ")
        lenduser = input("Enter the name of the user borrowing the book: ")
        self.lending_date = input("Enter the date the book is being lent: ")
        check=True
        for i in myBooks:
            if i.title == lendbook:
                for x in myUsers:
                    if x.username == lenduser:
                        check=False
                        self.book_id=i.book_id
                        self.user_id = x.user_id
            if check:
                print("Input unrecognized, try again.")
                self.lending_id=" "


    def return_book(self):
        self.return_date = input("Type the return date of the lent book: ")

    def display(self):
        print("Lending id: " + self.lending_id)
        print("Book id: " + self.book_id)
        print("User id: " + self.user_id)
        print("Lend date: " + self.lending_date)
        print("Return date: " + self.return_date)

myAuthors=[]
myBooks=[]
myLendList=[]
myUsers=[]

while 1:
    print("1. Add a book")
    print("2. Add an author")
    print("3. Add a user")
    print("4. Lend a book")
    print("5. Return a lent book")
    print("6. Display all books")
    print("7. Display all authors")
    print("8. Display all users")
    print("9. Display all books out for lending")
    print("99. exit")
    option=int(input("Choose from the menu what you want to do: "))

    if option==99:
        break
    elif option==1:
        b=Book()
        b.create_book()
        myBooks.append(b)
    elif option==2:
        a=Author()
        a.create_author()
        myAuthors.append(a)
    elif option==3:
        u=User()
        u.create_user()
        myUsers.append(u)
    elif option==4:
        l=Lend_Book()
        l.create_lend()
        myLendList.append(l)
    elif option==5:
        behave=5
        while behave==5:
            if len(myLendList)<1:
                print("No books are currently lent. Check your information.")
                break
            lentbook=input("Please type the lend id of the book being returned: ")
            check = True
            for y in myLendList:
                if y.lending_id == lentbook:
                    check = False
                    for z in myBooks:
                        if z.book_id == y.book_id:
                            sure=input("Is the name of the book "+z.title+"?")
                            if sure=="yes":
                                y.return_book()
                                behave=0
                            else:
                                print("Title doesn't match lend_id. Try again.")
                if check:
                    print("Input unrecognized, try again.")

    elif option==6:
        for i in range(0, len(myBooks)):
            print(f"-- {i+1} --")
            myBooks[i].display_book()
            print(" ")
    elif option==7:
        for i in range(0, len(myAuthors)):
            print(f"-- {i + 1} --")
            myAuthors[i].display()
            print(" ")
    elif option==8:
        for i in range(0, len(myUsers)):
            print(f"-- {i + 1} --")
            myUsers[i].display_user()
            print(" ")
    elif option==9:
        remove()
        for i in range(0, len(myLendList)):
            if myLendList[i].return_date==" ":
                print(f"-- {i + 1} --")
                myLendList[i].display()
                print(" ")
    else:
        print("Invalid input, try again.")