def login_register():
    name = input("Whats your name: ")
    print(f"Welcome {name}, You can:")
    while True:
        print("1.Register\n2.Login\n3.Exit")
        num = input("please choose operation number :")
        if not num.isdigit():
            print("please choose number from list: ")
            continue
        else:
            num = int(num)
            if num == 1:
                uname = input("Enter your username: ")
                pwd = input("Enter your password: ")
                email = input("Enter your email: ")
                file = open("file1.txt",'a')
                file.write(f"{uname},{pwd}\n")
                file.close()
                print("Register Successfully")
            elif num == 2:
                uname = input("Enter your username: ")
                pwd = input("Enter your password: ")
                file = open("file1.txt", 'r')
                list = file.read().split()
                f = False
                for i in list:
                    i = i.split(',')
                    if uname == i[0] and pwd == i[1]:
                        print("Login successfully")
                        f = True
                if f == False:
                    print("user not found, you should register at first")
                else:
                    break
            elif num == 3:
                break
login_register()


def replaceCoin():
    qty = float(input("Enter the Qty: "))
    print("Choose the type of coin you want 'replace from' :")
    print("1.USD\n2.SAR\n3.EUR")
    ch = int(input("Enter your chooies: "))
    print("choose the type of coin you want 'replace to' :")
    usd = 1.00
    sar = 3.75
    eur = 0.99
    res = 0.00
    one = "null"
    two = "null"
    if ch == 1:
        one = "USD"
        print("1.SAR\n2.EUR")
        ch2 = int(input("Enter your chooies: "))
        if ch2 == 1:
            two = "SAR"
            res = qty * sar
        elif ch == 2:
            two = "EUR"
            res = qty * eur
    elif ch == 2:
        one = "SAR"
        print("1.USD\n2.EUR")
        ch2 = int(input("Enter your chooies: "))
        if ch2 == 1:
            two = "USD"
            res = qty / sar
        elif ch == 2:
            two = "EUR"
            res = (qty / sar) * eur
    elif ch == 3:
        one = "EUR"
        print("1.USD\n2.SAR")
        ch2 = int(input("Enter your chooies: "))
        if ch2 == 1:
            two = "USD"
            res = qty / eur
        elif ch == 2:
            two = "SAR"
            res = (qty / eur) * sar
    print(f"{qty} {one} = {res:.2f} {two}")
        
replaceCoin()


def calc_price(price):
    tax_rate = price * 0.07
    return price + tax_rate

price = float(input("Enter the price: "))
print(calc_price(price))

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.is_borrowed = False

    def borrowBook(self):
        if self.is_borrowed == False:
            # print("Book borrowed successfully.")
            self.is_borrowed = True
            return True
        else:
            # print("Sorry, this book is currently not available.")
            return False
    
    def returnBook(self):
        if self.is_borrowed == True:
            print("Book returned successfully.")
            self.is_borrowed = False
            return True
        else:
            print("This book was not borrowed.")
            return False


# book1 = Book("Python Programming", "Ahmed Ali")
# book1.borrowBook()
# book1.borrowBook()
# book1.returnBook()
# book1.returnBook()


class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.books_borrowed = []

    def borrow_Book(self, book):
        if book.borrowBook():
            self.books_borrowed.append(book)
            print(f"{self.name} borrowed {book.name} book successfully")
        else:
            if book in self.books_borrowed:
                print("you really have this book")
            else:
                print("this book not available")

    def return_Book(self, book):
        if book in self.books_borrowed:
            if book.returnBook():
                self.books_borrowed.remove(book)
                print(f"{self.name} returned {book.name} book successfully")
        else:
            print(f"{self.name} does not have {book.name} book")

    def display_borrowed_books(self):
        if not self.books_borrowed:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"\n{self.name}'s borrowed books:")
            for book in self.books_borrowed:
                print(f"- {book.name} ", end=" ")


book1 = Book("programming", "Ahmed")
book2 = Book("C++", "anas")
book3 = Book("html", "mohamed")
book4 = Book("css", "tamer")
book5 = Book("js", "Ali")
book6 = Book("DB", "Khaled")
book7 = Book("Python", "saed")

member1 = Member("Ahmed Wael", 1)
member2 = Member("mohamed Wael", 2)

print("[1]", "-" * 20)
member1.borrow_Book(book1)  # Ahmed has book1
print("[2]", "-" * 20)
member1.borrow_Book(book2)  # Ahmed has book2
print("[3]", "-" * 20)
member2.borrow_Book(book1)  # can't
print("[4]", "-" * 20)
member1.return_Book(book1)  # Ahmed return book1
print("[5]", "-" * 20)
member2.borrow_Book(book1)  # mohamed has book1
print("[6]", "-" * 20)
member2.borrow_Book(book3)  # mohamed has book3
print("[7]", "-" * 20)
member1.borrow_Book(book1)  # can't
print("[8]", "-" * 20)
member1.borrow_Book(book4)  # Ahmed has book4
print("[9]", "-" * 20)
member1.borrow_Book(book5)  # Ahmed has book5
print("[10]", "-" * 20)
member2.borrow_Book(book6)  # mohamed has book6
print("[11]", "-" * 20)
member2.borrow_Book(book6)  # can't
print("[12]", "-" * 20)
member2.borrow_Book(book7)  # mohamed has book7
print("[13]", "-" * 20)

member1.display_borrowed_books() # 2 4 5
member2.display_borrowed_books() # 1 3 6 7

