import re
import csv
from datetime import datetime

# Book Class to represent a book in the library
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.book_id} | {self.title} by {self.author}"


# Library Class to manage books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(str(book) for book in self.books)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def save_books_to_csv(self, filename="books.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Book ID", "Title", "Author"])
            for book in self.books:
                writer.writerow([book.book_id, book.title, book.author])

    def load_books_from_csv(self, filename="books.csv"):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.books = [Book(row["Book ID"], row["Title"], row["Author"]) for row in reader]
        except FileNotFoundError:
            return "File not found."


# Helper Functions
def validate_book_id(book_id):
    """Validate Book ID using Regular Expressions"""
    pattern = r"^\d{3}-[A-Z]{3}$"
    return bool(re.match(pattern, book_id))


def add_sample_books(library):
    """Add some sample books to the library."""
    library.add_book(Book("101-ABC", "Python Basics", "John Doe"))
    library.add_book(Book("102-XYZ", "Data Science 101", "Jane Doe"))


# Testing Functions
def run_tests():
    library = Library()

    # Test Book Addition
    book = Book("123-ABC", "Test Book", "Test Author")
    library.add_book(book)
    assert len(library.books) == 1, "Book addition failed."

    # Test Book Search
    assert library.find_book("123-ABC") == book, "Book search failed."

    # Test Book ID Validation
    assert validate_book_id("123-ABC"), "Book ID validation failed."
    assert not validate_book_id("1234-ABCD"), "Book ID validation incorrectly passed."

    print("All tests passed!")


# Main Function
def main():
    library = Library()
    add_sample_books(library)

    while True:
        print("\n=== Library Management System ===")
        print("1. List Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Save to CSV")
        print("5. Load from CSV")
        print("6. Run Tests")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nBooks in Library:")
            print(library.list_books())
        elif choice == "2":
            book_id = input("Enter Book ID (e.g., 123-ABC): ")
            if not validate_book_id(book_id):
                print("Invalid Book ID format!")
                continue
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            library.add_book(Book(book_id, title, author))
            print("Book added successfully.")
        elif choice == "3":
            book_id = input("Enter Book ID to search: ")
            book = library.find_book(book_id)
            if book:
                print("Book Found:", book)
            else:
                print("Book not found.")
        elif choice == "4":
            library.save_books_to_csv()
            print("Books saved to CSV.")
        elif choice == "5":
            library.load_books_from_csv()
            print("Books loaded from CSV.")
        elif choice == "6":
            run_tests()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if name == "__main__":
    main()