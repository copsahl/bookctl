#!/usr/bin/env python3
import argparse
from sys import argv
from c_library import *
from c_book import Book

def main():

    if len(argv) < 2:
        parser.print_help()
        exit(0)

    lib = Library()

    if args.bookFlag == True and args.title != None and args.author != None:
        lib.addBook(Book(args.title, args.author))
    elif args.listBool == True:
        lib.listLibrary()
    elif args.removeBool == True and args.title != None:
        try:
            lib.removeBook(lib.getBook(args.title))
            print(f"Book \"{args.title}\" successfully removed!")
        except:
            print("Remove Error Occured")
    elif args.listFlag == True and args.listName != None and args.bookList != None:
        lib.addReadingList(args.listName, args.bookList)
    elif args.rList == True:
        lib.listAllReadingLists()
    elif args.rListAdd == True and args.listName != None and args.bookList != None:
        lib.listAddBooks(args.listName, args.bookList)
    elif args.purgeBool == True:
        lib.purge()
        exit(0)
    else:
        parser.print_help()
        exit(0)


    lib.cleanup()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--add-book', dest='bookFlag', action='store_true', default=False, help="Add a book. (Requires --title, --author)")
    parser.add_argument('--title', dest='title', type=str, default=None, help='Title of book.')
    parser.add_argument('--author', dest='author', type=str, default=None, help='Author of book')
    parser.add_argument('-l', '--list', dest='listBool', action='store_true', default=False, help="List all currently stored books.")
    parser.add_argument('-r', '--remove', dest='removeBool', action='store_true', default=False, help="Remove a given book form a list. (Requires --title)")
    parser.add_argument('--purge', dest='purgeBool', action='store_true', default=False, help="Erase all currently stored books and Reading lists.")
    parser.add_argument('--add-list', dest='listFlag', action='store_true', default=False, help="Add a reading list. (Requires --name and --book-list)")
    parser.add_argument ('--name', dest='listName', type=str, default=None, help='Name of new reading list.')
    parser.add_argument('--book-list', dest='bookList', nargs='+', default=[], help='Space separated list of books to add to a reading list.')
    parser.add_argument('-lr', '--listr', dest='rList', action='store_true', default=False, help="List currently stored reading list.")
    parser.add_argument('--listr-add', dest='rListAdd', action='store_true', default=False, help="Add book to existing rading list. (Requires --name and --book-list)")
    args = parser.parse_args()
    
    main()
