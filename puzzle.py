'''
a module to check if puzzle board meets requirements
https://github.com/alexg-lviv/puzzle
'''

def validate_rows(board: list):
    '''
    checks if colourful rows on board are filled correctly
    returns True if correct, False if not

    >>> validate_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *"])
    True
    '''
    for i in range(len(board)):
        my_string = board[i].strip("* ")
        for j in range(len(my_string)):
            if (my_string[j] != " ") and (my_string.count(my_string[j]) > 1):
                return False
    return True

def validate_columns(board: list):
    '''
    checks if colourful columns on board are filled correctly
    returns True if correct, False if not

    >>> validate_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *"])
    True
    '''
    result = []
    for i in range(len(board)):
        my_string = ''
        for j in range(len(board)):
            my_string += board[j][i]
        result.append(my_string)
    if validate_rows(result):
        return True
    return False

def validate_colours(board: list):
    '''
    checks if each colour is filled correctly
    returns True if correct, False if not

    >>> validate_colours(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "        "\
    , "         ", "         "])
    True
    '''
    i = 0
    j = 0
    new_board = []
    while i in range(len(board)-1):
        my_string = ""
        if board[j][i] != "*":
            z = j
            k = i
            while j < (z + 4):
                my_string += board[j][i]
                j += 1
            while k < (i + 5):
                if j >= 9:
                    break
                my_string += board[j][k]
                k += 1
            if j >= 9:
                break
            j = z + 1
            i = 0
            new_board.append(my_string)
        else:
            i += 1
    if validate_rows(new_board) == True:
        return True
    else:
        return False

def validate_board(board: list):
    '''
    main function, validates a puzzle board
    returns True if such board is winning, and False if not

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "         "\
    , "         ", "         "])
    True
    '''
    if validate_rows(board) and validate_columns(board) and validate_colours(board):
        return True
    return False


if __name__ == "__main__":
	board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   2  **",
 "  8  2***",
 "  2  ****"
]
	print("hello world!")