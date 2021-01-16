# Asks user for the number of rows, columns, and number of words
# Prints out a crossword puzzle of the specified size with all possible word inclusions

def printboard(board):
    '''
    Prints out the  board provided in a readible format.
    :param board: board array
    :return: None
    '''

    for i in range(len(board)):
        print('[',end="")
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                print(' ', end="")
            else:
                print(board[i][j], end="")  # prints out the body of the board
            print('|', end="") if j < len(board[0])-1 else print(']')


def addFirstWord(board, word):
    '''
    Returns a boolean value specifying if the word was added to the middle center of the board.
    :param board: board array
    :param word: word to be added
    :return: True/False
    '''

    brows, bcols, w = len(board), len(board[0]), len(word)
    row = (brows - 1) // 2  # row to add first word to
    col = bcols // 2 - w // 2  # column to start adding from

    if w > brows:
        return False
    else:
        for a in range(w):
            board[row][col + a] = word[a]
        return True


def find(board, word):
    '''
    Finds and returns all locations where each of the letters in the word occur in the board.
    :param board: array for puzzle board
    :param word: word to be matched
    :return: True/False, all matching locations
    '''

    locs = []  # tracks all locations where there's a matching letter

    # checks the board to find matching locations for every letter in the word
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in word:
                locs.append([i, j])

    # returns the locations
    if len(locs) == 0:
        return False, locs
    else:
        return True, locs


def checkvertical(board, word, row, col):
    '''
    Returns a boolean value specifying if the word provided can be added to the board vertically.
    :param board: board array
    :param word: word to be checked
    :param row: row to be checked
    :param col: column to be checked
    :return: True/False, code
    '''

    w, b = len(word), len(board)
    intersect, side = False, False
    match, index = [], [i for i in range(w)]

    # legal row, col values check:
    if row < 0 or row > len(board)-1 or col < 0 or col > len(board[0])-1:
        raise NameError('Illegal row and column values')

    # checks to make sure the words fits the board
    if w > (b - row):
        return False

    #  # checks to make sure all intersections are legal or with blank spaces
    for i in range(w):
        if board[row + i][col] == word[i]:
            match.append(i)  # tracks all intersection indices
            intersect = True
        elif board[row + i][col] != ' ' and board[row + i][col] != word[i]:
            return False  # rejects the (row, col) if any spaces equal another letter

    if not intersect:
        return False
    else:
        # removes intersection indices from the end
        match.reverse()
        for i in match:
            del index[i]

    # checks to make sure there are no letters at the top or bottom of the word
    if row == 0 and w < b:
        if board[row + w][col] != ' ':
            side = True
    elif row > 0 and (row + w) < b:
        if board[row - 1][col] != ' ' or board[row + w][col] != ' ':
            side = True
    elif row > 0 and (row + w) == b:
        if board[row - 1][col] != ' ':
            side = True

    # checks to make sure there's no letter on either side of where each letter of the word (apart from
    # the intersecting letters) will be placed to ensure no illegal words are formed
    for i in index:
        if col == 0:
            if board[row + i][col + 1] != ' ':
                side = True
        elif col < (len(board[0]) - 1):
            if board[row + i][col - 1] != ' ' or board[row + i][col + 1] != ' ':
                side = True
        elif col == (len(board[0]) - 1):
            if board[row + i][col - 1] != ' ':
                side = True

    # returns if the word can be legally placed in the board
    if side:
        return False
    else:
        return True  # passes all checks


def checkhorizontal(board, word, row, col):
    '''
    Returns a boolean value specifying if the word provided can be addded to the board horizontally.
    :param board: board array
    :param word: word to be checked
    :param row: row to be checked
    :param col: column to be checked
    :return: True/False, code
    '''

    w, b = len(word), len(board[0])
    intersect, side = False, False
    match, index = [], [i for i in range(w)]

    # legal row, col values check:
    if row < 0 or row > len(board)-1 or col < 0 or col > len(board[0])-1:
        raise NameError('Illegal row and column values')

    # checks to make sure the word fits the board
    if w > (b - col):
        return False

    # checks to make sure all intersections are legal or with blank spaces
    for i in range(w):
        if board[row][col + i] == word[i]:
            match.append(i)
            intersect = True
        elif board[row][col + i] != ' ' and board[row][col + i] != word[i]:
            return False

    if not intersect:
        return False
    else:
        # removes intersection indices from the end
        match.reverse()
        for i in match:
            del index[i]

    # checks to make sure there are no letters on either side of the word
    if col == 0 and w < b:
        if board[row][col + w] != ' ':
            side = True
    elif col > 0 and (col + w) < b:
        if board[row][col - 1] != ' ' or board[row][col + w] != ' ':
            side = True
    elif col > 0 and (col + w) == b:
        if board[row][col - 1] != ' ':
            side = True

    # checks to make sure there's no letter above or below where each letter of the word (apart from the
    # intersecting letters) will be placed to ensure no illegal words are formed
    for b in index:
        if row == 0:
            if board[row + 1][col + b] != ' ':
                side = True
        elif row < (len(board) - 1):
            if board[row - 1][col + b] != ' ' or board[row + 1][col + b] != ' ':
                side = True
        elif row == (len(board) - 1):
            if board[row - 1][col + b] != ' ':
                side = True

    # returns if the word can be legally placed in the board
    if side:
        return False
    else:
        return True  # passes all checks


def addvertical(board, word):
    '''
    Returns a boolean value specifying if the word provided was added to the board vertically.
    :param board: board array
    :param word: word to be added
    :return: True/False, code
    '''

    w, b = len(word), len(board)
    matches = -1
    fit = False

    # locate returns whether there are any matching letters; locs returns their locations if there are any
    locate, locs = find(board, word)

    if not locate:
        return False

    # cycles through each of the location matches until it finds one that works
    # loops exits once a match is found or if all possibilities have been checked
    while not fit and matches < len(locs) - 1:
        matches += 1
        row = locs[matches][0]
        col = locs[matches][1]

        # determines start and end row numbers for each location match
        # start = row number for the first letter if the last letter of the word was placed in the location match
        # end = row number for the last letter if the first letter of the word was placed in the location match
        if (row - w + 1) > 0:
            start = row - w + 1
        elif (row - w + 1) <= 0:
            start = 0

        if (row + w - 1) < b:
            end = row + w - 1
        elif (row + w - 1) >= b:
            end = b - 1

        # starts checking from the bottom most row
        r = end + 1

        # checks to make sure the word fits legally
        while not fit and r > start:
            r -= 1
            fit = checkvertical(board, word, r, col)

    # adds word to the board if possible and returns True or returns False
    if fit:
        row = r
        for i in range(len(word)):
            board[row + i][col] = word[i]
        return True
    else:
        return False


def addhorizontal(board, word):
    '''
    Returns a boolean value specifying if the word provided was added to the board horizontally.
    :param board: board array
    :param word: word to be added
    :return: True/False
    '''

    w, b = len(word), len(board[0])
    matches = -1
    fit = False

    # locate returns whether there are any matching letters; locs returns their locations if there are any
    locate, locs = find(board, word)

    if not locate:
        return False

    # cycles through each of the location matches until it finds one that works
    while not fit and matches < len(locs) - 1:
        matches += 1
        row = locs[matches][0]
        col = locs[matches][1]

        # determines start and end column numbers for each location match
        # start = column number for the first letter if the last letter of the word was placed in the location match
        # end = column number for the last letter if the first letter of the word was placed in the location match
        if (col - w + 1) > 0:
            start = col - w + 1
        elif (col - w + 1) <= 0:
            start = 0


        if (col + w - 1) < b:
            end = col + w - 1
        elif (col + w - 1) >= b:
            end = b - 1

        # starts checking from the right most column
        c = end + 1

        # checks to make sure the word fits
        while not fit and c > start:
            c -= 1
            fit = checkhorizontal(board, word, row, c)

    # adds word to the board if possible and returns True or returns False
    if fit:
        col = c
        for i in range(len(word)):
            board[row][col + i] = word[i]
        return True
    else:
        return False


def addwords(board, L):
    '''
    Attempts to add each of the words in the list L vertically and/or horizontally once to the board and returns a
    list of words that could not be added.
    :param board: board array
    :param L: list of words to be added
    :return: list of words that could not be added
    '''

    recheck = []
    a = 0

    # adds first word to the board horizontally in the middle center and then alternates direction
    # between vertical and horizontal for each following word that can be added to the board
    for word in L:
        if a == 0:  # adds first word in the list
            result = addFirstWord(board, word)
            if not result:
                recheck.append(word)  # stores first word that could not be added
            else:
                # only attempts to add the next word vertically if first word was placed
                a += 1
                vertical = True
        elif vertical:  # adds word vertically to the board
            result = addvertical(board, word)
            if not result:
                # attempts to add word horizontally if it could not be added vertically
                result = addhorizontal(board, word)
                if not result:
                    recheck.append(word)  # stores words that could not be added in either direction
            else:
                # toggles on horizontal direction if previous word was added vertically
                vertical = False
            a += 1
        elif not vertical:  # adds word horizontally to the board
            result = addhorizontal(board, word)
            if not result:
                # attempts to add word vertically if it could not be added horizontally
                result = addvertical(board, word)
                if not result:
                    recheck.append(word)  # stores words that could not be added in either direction
            else:
                # toggles on vertical direction if previous word was added horizontally
                vertical = True
            a += 1

    # returns list of words that could not be added to the board
    return recheck


def readdwords(board, L):
    '''
    Adds all the words in list L that can be added to the board and returns words that cannot be added. It differs
    from function addwords(board, L) because it does not attempt to add the first word to the middle-center.
    :param board: board array
    :param L: list of words to be added
    :return: list of words that could not be added
    '''

    recheck = []

    # tries to add each word in the list to the board in both directions
    for word in L:
        result = addvertical(board, word)
        if not result:
            result = addhorizontal(board, word)
            if not result:
                recheck.append(word)  # stores words that could not be added

    # returns a list of words that cannot be added
    return recheck


def crossword(L, maxrows, maxcols):
    '''
    Attempts to make a crossword puzzle using the given list of words
    :param L: list of words to be added to the crossword puzzle
    :return: None
    '''

    board = [[' '] * maxcols for i in range(maxrows)]
    recheck = addwords(board, L)
    oldlen = len(recheck)  # length of old words to be rechecked
    newlen = -1  # length of new words to be rechecked

    # rechecks words that didn't fit in the first try
    if oldlen > 0:
        # loop exists if the new list of words to be rechecked is identical to the old list
        while oldlen != newlen:
            recheck = readdwords(board, recheck)
            newlen = len(recheck)

            if newlen == 0:
                oldlen = newlen
            elif newlen != oldlen:
                oldlen = newlen
                newlen = -1

    # prints out words that could not added (if any) and the crossword puzzle
    if oldlen != 0:
        print('Crossword Puzzle')
        print(' ')
        printboard(board)
        print(' ')
        print('These word(s) could not be added:', recheck)
        print(' ')
    else:
        print('Crossword Puzzle')
        print(' ')
        printboard(board)
        print(' ')

# Main program
setUp = 0

while (setUp != 1):
    print('Welcome to the Crossword Creator!')
    print('Please enter the crossword board size you desire.')
    print('Number of rows: ', end="")
    rows = input()
    print('Number of columns: ', end="")
    cols = input()
    print('How many words would you like to add? ', end="")
    numofw = input()

    L = [];

    if (rows.isdigit() and cols.isdigit() and numofw.isdigit()):
        validChoice = 0
        while (validChoice != 1):
            print("Enter 0 to submit words on the same line or 1 for different lines: ", end="")
            choice = input()
            if (choice == '0' or choice == '1'):
                validChoice = 1
            else:
                print('You have entered an invalid choice selection.')

        if int(choice) == 1:
            for nums in range(0, int(numofw)):
                print('Please enter a word: ', end="")
                word = input()
                L.append(word)
        else:
            print('Please enter each word separated by a comma (no spaces): ', end="")
            words = input()
            L = words.split(',', int(numofw))

        print(' ')
        setUp = 1
    else:
        print('You have entered an invalid number of rows, columns, or words.')

crossword(L, int(rows), int(cols))
