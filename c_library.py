#TODO: Adapt reading list functionality to allow for multiple lists
#TODO: When you remove a book form library, remove it from reading list

import ast
from c_book import Book
from c_readinglist import ReadingList
import json
from os.path import exists
from os import stat, remove

BOOK_FILE = "data/books.json"
LIST_FILE = "data/readinglists.json"

class Library:

    def __init__(self):

        self.library = list()
        self.readingList = None

        # Read in book data (if available)
        if exists(BOOK_FILE) and stat(BOOK_FILE).st_size > 5:
            with open(BOOK_FILE) as fObj:
                data = json.load(fObj)
            for book in data:
                self.library.append(Book(book['title'], book['author']))
    
        if exists(LIST_FILE) and stat(LIST_FILE).st_size > 5:
            with open(LIST_FILE) as fObj:
                data = json.load(fObj)
            
            self.readingList = ReadingList(data['name'])
            for i in range(1, len(data['books']) + 1):
                self.readingList.books[str(i)] = data['books'][str(i)]


    def addBook(self, book):
        self.library.append(book)

    def getBook(self, title):
        for book in self.library:
            if book.title == title:
                return book
        raise BookNotFoundError

    def removeBook(self, book):
        try:
            self.library.remove(book)
        except ValueError:
            raise BookRemoveError

    def listLibrary(self):
        for book in self.library:
            print(f"{book.title}\nby {book.author}\n")

    def addReadingList(self, name, books):
        """
        Books will be a list of dict's ie [{'title': 'test', 'author': 'test'},]
        """
        newBooks = []

        for book in books:
            try:
                newBooks.append(self.getBook(book).__dict__)
            except:
                print(f"Failed to add {book} to reading list! Book not found!")
                continue

        self.readingList = ReadingList(name)
        index = 1
        for d in newBooks:
            self.readingList.books[str(index)] = d
            index += 1

    def listAllReadingLists(self):
        if self.readingList == None:
            return

        print(f"--[{self.readingList.name}]--")
        for k, v in self.readingList.books.items():
            print(f"{k}. {v['title']} by {v['author']}")

    def listAddBooks(self, name, books):
        index = len(self.readingList.books) + 1
        for book in books:
            try:
                self.readingList.books[str(index)] = self.getBook(book).__dict__
            except:
                print(f"Failed to add new book {book} to {name}!")

    def purge(self):
        try:
            remove(BOOK_FILE)
        except FileNotFoundError:
            pass
        try:
            remove(LIST_FILE)
        except FileNotFoundError:
            pass

    def cleanup(self):
        """
        Dump book data JSON
        Dump reading list data to JSON
        """
        # Books
        if len(self.library) > 0:
            jsonBooks = json.dumps([book.__dict__ for book in self.library])
            with open(BOOK_FILE, 'w') as bookFile:
                bookFile.write(jsonBooks)

        if self.readingList !=  None:
            jsonLists = json.dumps(self.readingList.__dict__)
            with open(LIST_FILE, 'w') as listFile:
                listFile.write(jsonLists)
