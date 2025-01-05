class Book:
    def __init__(self, title, author):
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.available = True  # Availability status of the book (True if available, False if checked out)

    def checkout(self):
        if self.available:
            self.available = False
            print(f"'{self.title}' by {self.author} has been checked out.")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        """Return the book and mark it as available."""
        if not self.available:
            self.available = True
            print(f"'{self.title}' by {self.author} has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

    def display_info(self):
        """Display information about the book."""
        availability = "Available" if self.available else "Checked out"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {availability}\n")


class LibraryCatalogue:
    def __init__(self):
        self.books = []  # List to hold book objects

    def add_book(self, book):
        """Add a book to the library catalogue."""
        self.books.append(book)
        print(f"'{book.title}' has been added to the catalogue.\n")

    def display_all_books(self):
        """Display information about all books in the catalogue."""
        if not self.books:
            print("No books in the catalogue.")
        else:
            for book in self.books:
                book.display_info()

    def find_book_by_title(self, title):
        """Find a book by its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None



if __name__ == "__main__":
    # Create a few book objects
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    library = LibraryCatalogue()

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Library Catalogue:\n")
    library.display_all_books()

    book1.checkout()
    
    book1.checkout()

    book1.return_book()

    print("\nUpdated Library Catalogue:\n")
    library.display_all_books()

    book_to_find = library.find_book_by_title("The Great Gatsby")
    if book_to_find:
        print(f"\nFound Book:\n{book_to_find.display_info()}")
    else:
        print("\nBook not found.")
