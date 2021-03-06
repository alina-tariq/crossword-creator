# Crossword Creator

## Language
* Python

## What Is It? 
- A command line python program that allows you to create a crossword puzzle from a list of words
- The user is asked for the following input prior to generating a crossword puzzle:
	* size of the crosswords (rows x columns)
	* numbers of words to be added
	* the theme of the crossword
	* how words will be provided (i.e. entered on a single line separated by a comma or entered on different lines)
	* the words (entered in ALL CAPS)
- The program then prints the crossword puzzle with the theme at the top, noting at the end any words that could not be added to the crossword without breaking the rules
- The rules are as follows:
	* each word must intersect with at least one other word
	* no illegal words (side by side letters that don't form a crossword word) can exist

## How To Use
Use the following commands to run the program:
```
git clone https://github.com/alina-tariq/crossword-creator.git
cd crossword-creator
python3 crossword.py
```

## Upcoming Features
[ ] Adding numbers to the words in the crossword printout  
[ ] The ability to request accompanying clues from the user and print 

## Demo
![Demo 1](./demo/demo-1.png)
![Demo 2](./demo/demo-2.png)
