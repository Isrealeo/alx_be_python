class Book:
    def __init__ (self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self.is_checked_out = 0
    
    def check_out(self):
        if not self.is_check_out:
            self.check_out True
            return True
        return False
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    def is_available(self):
        return not self.is_check_out
    
class Library:
    """A class representing a library."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book object to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Book '{book.title}' by {book.author} added to the library.")
        else:
            print("Error: Only Book instances can be added.")

    def check_out_book(self, title):
        """Check out a book if available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"You checked out '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                    return
                else:
                    print(f"'{book.title}' was not checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def list_available_books(self):
        """List all available books."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
        else:
            for book in available:
                print(f"- {book.title} by {book.author}")
        
