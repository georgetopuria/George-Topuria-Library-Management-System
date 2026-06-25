#main "controller"
#mtavari kodi
from book import Book
from member import Member
from library import Library
#menu interfacr
def show_menu():
    print("\nLibrary Management System")
    print("1. aAdd Book")
    print("2. add Member")
    print("3. view Books")
    print("4. View members")
    print("5. borrow book")
    print("6. return book")
    print("7. view loans")
    print("8. Save and Exit")


def main():
    library = Library()

    while True:
        show_menu()
        choice = input("choose an Option: ")
#trial
#mcdeloba
        try:
            if choice == "1":
                book_id = input("book ID: ")
                title = input("Title: ")
                author = input("author: ")
                genre = input("Genre: ")
                year = input("year: ")

                book = Book(book_id, title, author, genre, year)
                library.add_book(book)
                print("book added Successfully.")

            elif choice == "2":
                member_id = input("member iD: ")
                name = input("Name: ")
                email = input("email: ")

                member = Member(member_id, name, email)
                library.add_member(member)
                print("member added Successfully.")

            elif choice == "3":
                for book in library.books:
                    print(book)

            elif choice == "4":
                for member in library.members:
                    print(member)

            elif choice == "5":
                book_id = input("book ID: ")
                member_id = input("Member id: ")

                library.borrow_book(book_id, member_id)
                print("book Borrowed Successfully.")

            elif choice == "6":
                book_id = input("Book ID: ")

                library.return_book(book_id)
                print("Book Returned successfully.")

            elif choice == "7":
                for loan in library.loans:
                    print(loan)

            elif choice == "8":
                library.save_all()
                print("Data saved. goodbye.")
                break

            else:
                print("Invalid option. olease choose 1-8.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()