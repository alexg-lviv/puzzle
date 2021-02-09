def validate_rows(board: list):
    '''
    checks if colourful rows on board are filled correctly
    returns True if correct, False if not
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
    '''
    pass

def validate_colours(board: list):
    '''
    checks if each colour is filled correctly
    returns True if correct, False if not
    '''
    pass


def validate_board(board: list):
    '''
    main function, validates a puzzle board
    returns True if such board is winning, and False if not
    '''
    pass


if __name__ == "__main__":
	board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]
	print(validate_rows(board))