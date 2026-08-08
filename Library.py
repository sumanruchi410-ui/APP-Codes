# Library Management System using OOP in Python

# Class to represent a Book
class Book:
    # Constructor to initialize book details
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True   # Book is available by default

    # Method to display book information
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"


# Class to represent a Library Patron (User)
class Patron:
    # Constructor to initialize patron details
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []   # List to store borrowed books

    # Method to display patron information
    def __str__(self):
        return f"ID: {self.patron_id}, Name: {self.name}"


# Class to manage the Library
class Library:
    # Constructor to initialize dictionaries for books and patrons
    def __init__(self):
        self.books = {}      # Stores books using book_id as key
        self.patrons = {}    # Stores patrons using patron_id as key

    # Method to add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    # Method to register a new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    # Method to borrow a book
    def borrow_book(self, patron_id, book_id):

        # Check if patron exists
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        # Check if book exists
        if book_id not in self.books:
            print("Book not found.")
            return

        # Get book and patron objects
        book = self.books[book_id]
        patron = self.patrons[patron_id]

        # Check if the book is available
        if book.is_available:
            book.is_available = False
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is currently unavailable.")

    # Method to return a borrowed book
    def return_book(self, patron_id, book_id):

        # Check if patron exists
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[patron_id]

        # Search for the borrowed book
        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.is_available = True
                patron.borrowed_books.remove(book)
                print(f"{patron.name} returned '{book.title}'.")
                return

        print("Book was not borrowed by this patron.")

    # Method to display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(book)

    # Method to display all registered patrons
    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            print(patron)


# Main Program 

# Create a Library object
library = Library()

# Add books to the library
library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Alice Brown"))
library.add_book(Book(103, "Machine Learning", "David Lee"))

# Register library patrons
library.register_patron(Patron(1, "Rahul"))
library.register_patron(Patron(2, "Priya"))

# Display all books
library.display_books()

# Borrow books
library.borrow_book(1, 101)
library.borrow_book(2, 102)

# Display books after borrowing
library.display_books()

# Return a borrowed book
library.return_book(1, 101)

# Display books after returning
library.display_books()

# Display all registered patrons
library.display_patrons()