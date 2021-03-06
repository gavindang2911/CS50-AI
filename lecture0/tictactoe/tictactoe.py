"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
    	for cell in row:
    		if cell != EMPTY:
    			count++

    if count%2 == 0:
    	return X
    else
    	return O 



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i, row in enumerate(board):
    	for j, cell in enumerate(row):
    		if cell == EMPTY:
    			result.add((i,j))


    return result



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
    	raise ValueError("Gamve over!")
    elif action not in actions(board):
    	raise ValueError("Invalid action")
    else:
    	player = player(board)
    	resultBoard = deepcopy(board)
    	i,j = action
    	resultBoard[i][j] = player

    return resultBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
