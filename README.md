# ./bookctl.py

Command Line Tool to help organize your reading.

## How it works

1. Add Books
	- `./bookctl.py --add-book --title "Perelandra" --author "C.S. Lewis"`
	
2. Create New Reading List
	- `./bookctl.py --add-list --name "Summer 2021" --book-list "Perelandra"`

3. Continue to add to the reading list
	- `./bookctl --listr-add --name --book-list "That Hideous Strength"`

*All data is stored in data/FILENAME.json*

### Note:
*You can only add books to a list that you have ALREADY added to your library.*

### Future Additions:
	- Multiple Reading Lists
	- Quicker, more convenient, CLI Args
	- Search and sort functionality (Author, genre). 

### Bugs:
	- Reading list can contain books deleted from library
	- Pretty much the whole program. It's just one big bug. 
