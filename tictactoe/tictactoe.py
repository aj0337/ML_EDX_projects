"""
Tic Tac Toe Player
"""

import math
import numpy as np
import copy

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

    if board == initial_state():
        return X
    if board == terminal(board):
        return X
    else:
        X_count = 0
        O_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    X_count += 1
                
                elif board[i][j] == 'O':
                    O_count += 1
        if X_count == O_count:
            return X
        else:
            return O
        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    if terminal(board):
        return ((0,0))

    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                actions.add((i,j))
                
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)

    #if board[action[0]][action[1]]:
        #raise Exception('action not allowed')
    try:
        i = action[0]
        j = action[1]
        board_copy[i][j] = player(board)
    except IndexError:
         raise

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board = np.array(board)
    for i in range(3):
        if((board=='X').all(axis=1)).any()==True:
            return X
        elif((board=='O').all(axis=1)).any()==True:
            return O
    for j in range(3):
        if((board=='X').all(axis=0)).any()==True:
            return X
        elif((board=='O').all(axis=0)).any()==True:
            return O    
    if board[0,0]==board[1,1]==board[2,2]=='X':
        return X
    elif board[0,0]==board[1,1]==board[2,2]=='O':
        return O
    elif board[0,2]==board[1,1]==board[2,0]=='X':
        return X
    elif board[0,2]==board[1,1]==board[2,0]=='O':
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) == X:
        return True
    elif winner(board) == O:
        return True
    else:
        return False
    
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = np.inf
    
    for action in actions(board):
        v = min(v,maxvalue(result(board,action)))
       
    return v

def maxvalue(board):

    if terminal(board):
        return utility(board)
    v = -np.inf
    
    for action in actions(board):
        v = max(v,minvalue(result(board,action)))
        
    return v       

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == 'X':
        move = set()
        v_temp = -np.inf
        for action in actions(board):
            v = minvalue(board)
            if v > v_temp:
                v_temp = v
                move = action
        
    elif player(board) == 'O':
        move = set()
        v_temp = np.inf
        for action in actions(board):
            v = maxvalue(board)
            if v < v_temp:
                v_temp = v
                move = action
        
    return move