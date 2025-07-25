class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            # print(f"Title: {book.title}, Author: {book.author}")
            return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("My Library")
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "Jane Austen")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
print(library.list_books())

for book in library.list_books():
    print(book)