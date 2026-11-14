
# Library Management System


# Creating Book Class

class Book:

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity


# Creating Library Class

class Library:

    def __init__(self):
        self.books = {}
        self.issued_books = []

    # Function to Add Book

    def add_book(self):

        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("This Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        quantity = int(input("Enter Quantity: "))

        # Check quantity
        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        new_book = Book(book_id, title, author, quantity)

        self.books[book_id] = new_book

        print("Book added successfully!")

    # Function to View All Books

    def view_books(self):

        if not self.books:
            print("No books available!")
            return

        for book_id, book in self.books.items():

            print("------------------------")
            print("Book ID:", book_id)
            print("Book Title:", book.title)
            print("Author:", book.author)
            print("Quantity:", book.quantity)

   # Function to Search Book

    def search_book(self):

                search = input("Enter Book ID or Book Title: ")

                found = False

                for book_id, book in self.books.items():

                    if book_id == search or book.title.lower() == search.lower():
                        print("------------------------")
                        print("Book Found!")
                        print("Book ID:", book.book_id)
                        print("Book Title:", book.title)
                        print("Author:", book.author)
                        print("Quantity:", book.quantity)

                        found = True
                        break

                if not found:
                    print("Book not found!")

    # Function to Issue Book

    def issue_book(self):

        book_id = input("Enter Book ID to Issue: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        if self.books[book_id].quantity <= 0:
            print("Book is not available!")
            return

        student_name = input("Enter Student Name: ")

        self.books[book_id].quantity -= 1

        self.issued_books.append({
            "book_id": book_id,
            "student_name": student_name
        })

        print("Book issued successfully!")
        print("Student Name:", student_name)
        print("Remaining Quantity:", self.books[book_id].quantity)

    # Function to View Issued Books

    def view_issued_books(self):

        if not self.issued_books:
            print("No books have been issued!")
            return

        for record in self.issued_books:

            book_id = record["book_id"]
            student_name = record["student_name"]

            print("------------------------")
            print("Book ID:", book_id)
            print("Book Title:", self.books[book_id].title)
            print("Student Name:", student_name)

            # Function to Return Book

    def return_book(self):

                book_id = input("Enter Book ID to Return: ").strip()
                student_name = input("Enter Student Name: ").strip()

                for record in self.issued_books:

                    if (record["book_id"] == book_id and
                            record["student_name"].lower() == student_name.lower()):
                        self.issued_books.remove(record)

                        self.books[book_id].quantity += 1

                        print("Book returned successfully!")
                        print("Updated Quantity:", self.books[book_id].quantity)
                        return

                print("No matching issued book record found!")
                # Function to Delete Book

    def delete_book(self):

        book_id = input("Enter Book ID to Delete: ").strip()

        if book_id not in self.books:
            print("Book not found!")
            return

        for record in self.issued_books:

            if record["book_id"] == book_id:
                print("Cannot delete! This book is currently issued.")
                return

        del self.books[book_id]

        print("Book deleted successfully!")


# Creating Library Object



my_library = Library()

# Main Menu

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. View Issued Books")
    print("6. Return Book")
    print("7. Delete Book")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        my_library.add_book()

    elif choice == "2":
        my_library.view_books()

    elif choice == "3":
        my_library.search_book()

    elif choice == "4":
        my_library.issue_book()

    elif choice == "5":
        my_library.view_issued_books()

    elif choice == "6":
        my_library.return_book()

    elif choice == "7":
        my_library.delete_book()

    elif choice == "8":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please select 1 to 8.")