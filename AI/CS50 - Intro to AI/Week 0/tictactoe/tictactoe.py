"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
ROWS = 3
COLS = 3

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# def initial_state():
#     """
#     Returns starting state of the board.
#     """
#     return [["X", EMPTY, "X"],
#             ["O", EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    # If the board is in the terminal state, return "Game Over"
    if terminal(board):
        return "Game Over"
    
    # Initialize the number of turns each
    x_turns = 0
    o_turns = 0
    # Count how many turns each player has gone
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "X":
                x_turns += 1
            elif board[r][c] == "O":
                    o_turns += 1
    
    # If X has more turns, then it is O's turn
    if x_turns > o_turns:
        return "O"
    # Otherwise it is X's turn
    else:
        return "X"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    # If the board is in a terminal state, return no actions
    if terminal(board):
        return "Game Over"
    
    # Create an empty set
    available_moves = set()
    # Add any available moves to the set
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == None:
                available_moves.add((r, c))
    
    # Return the set of possible moves
    return available_moves
            

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # Check to make sure it is a valid move
    if (action[0] < 0 or action[0] > 2) or (action[1] < 0 or action[1] > 2): 
        raise Exception("Invalid Move")
    
    # Make a copy of the board
    board_copy = copy.deepcopy(board)
    
    # Change the spot from the action to be that 
    # of the player whos turn it is
    board_copy[action[0]][action[1]] = player(board)
    
    # Return that copy
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check each Row for a winner
    for r in range(ROWS):
        if None not in board[r] and len(set(board[r])) == 1:
            return 'O' if 'O' in set(board[r]) else 'X'
    
    # Check each Column for a winner
    for c in range(COLS):
        col = (board[0][c], board[1][c], board[2][c])
        if None not in col and len(set(col)) == 1:
            return 'O' if 'O' in set(col) else 'X'
        
    # Check each DIAG for a winner
    diag1 = (board[0][0], board[1][1], board[2][2])
    if None not in diag1 and len(set(diag1)) == 1:
        return 'O' if 'O' in set(diag1) else 'X'
    diag2 = (board[0][2], board[1][1], board[2][0])
    if None not in diag2 and len(set(diag2)) == 1:
        return 'O' if 'O' in set(diag2) else 'X'
    
    # If nothing returns by now, there are no winners
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # Has the game been won? If yes, return True
    if winner(board) != None:
        return True
    # Are there any spots left? 
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == None:
                return False
    # Otherwise return false - Game is still in progress
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    # Is the game in a terminal state?
    if terminal(board) == False:
        raise Exception("Game is not over... keep playing")
    
    # Return 1 if X has won
    if winner(board) == "X":
        return 1
    # Return -1 if O has won
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    # If the board is in a terminal state, return None
    if terminal(board):
        return None
    
    if player(board) == "X": # then we need to start with a max
        history = minimax_2(board, "max")
        val = -2
        for i in range(len(history)):
            if history[i][1] >= val:
                val = history[i][1]
                move = history[i][0]
    else:
        history = minimax_2(board, "min")
        val = 2
        for i in range(len(history)):
            if history[i][1] <= val:
                val = history[i][1]
                move = history[i][0]
    
    return move

def minimax_2(board, switch):
    """
    Returns the optimal move
    """
    
    history = []
    
    if switch == "max":
        for action in actions(board): 
            # Take the first step
            tmp_board = result(board, action)
            if terminal(tmp_board):
                value = utility(tmp_board)
            else:
                value = float('-inf')
                value = max(value, min_o(result(tmp_board, action)))
            
            history.append((action, value))
    else: 
        for action in actions(board): 
            # Take the first step
            tmp_board = result(board, action)
            if terminal(tmp_board):
                value = utility(tmp_board)
            else:
                value = float('inf')
                value = min(value, max_x(result(tmp_board, action)))
            
            history.append((action, value))
    
    return history
    

def max_x(board):
    """
    Returns the optimal move for X
    """
    
    # If terminal board, return the utility of the board
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        # create a value of -infinity
        value = float('-inf')
        value = max(value, min_o(result(board, action)))
    
    return value
    

def min_o(board):
    """
    Returns the optimal move for O
    """
    
    # If terminal board, return the utility of the board
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        # create a value of -infinity
        value = float('inf')
        value = min(value, max_x(result(board, action)))
    
    return value
