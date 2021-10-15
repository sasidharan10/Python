class library:
    books = ["THINK AND GROW RICH", "RICH DAD POOR DAD", "ATOMIC HABITS",
             "ALCHEMIST", "INFLUENCE PEOPLE", "SUBCONSCIOUS MIND"]

    Issuedbooks = {}

    def __init__(self, ls, libname) -> None:
        self.books.extend(ls)
        self.libname = libname

    def displaybook(self):
        i = 1
        print("\nList Of Books : \n")
        for book in self.books:
            print(f"{i}) {book}")
            i += 1

    def addbook(self, add):
        self.books.extend(add)
        print("Book added Successfully!")

    def lendbook(self, book, name):
        self.Issuedbooks.update({book: name})
        print("Book Issued Sucessfully")
        self.available()

    def available(self):
        print("\nAvailable Books : \n")
        if bool(self.Issuedbooks) == False:
            self.displaybook()
            return
        i = 1
        for b in self.books:
            if b not in self.Issuedbooks:
                print(f"{i}) {b}")
                i += 1

    def returnbook(self, book):
        self.Issuedbooks.pop(book)
        print("Book Returned Successgully!")


if __name__ == "__main__":
    l = library(["7 Habits"], "Happy")
    l.displaybook()
    print(f"\n-----WELCOME TO {(l.libname).upper()} LIBRARY-----\n")
    print("Availabe Operations : \n")
    print("1) Show Books")
    print("2) Add Books")
    print("3) Issue Books")
    print("4) Return Books")
    print("5) Available Books")
    while(True):
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            l.displaybook()
        elif ch == 2:
            bk = input("Enter Book to Add : ").upper()
            l.addbook([bk])
        elif ch == 3:
            l.available()
            nm = input("Enter Your Name : ").upper()
            bk = input("Enter Book name to Issue : ").upper()
            l.lendbook(bk, nm)
        elif ch == 4:
            bk = input("Enter Book name to Return : ").upper()
            l.returnbook(bk)
            l.available()
        elif ch == 5:
            l.available()
        else:
            break
print("\n-----Thanks for visiting our Library-----\n")
