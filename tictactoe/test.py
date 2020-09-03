from tictactoe import *

X = "X"
O = "O"
EMPTY = None

board= [['X', 'O', 'X'],
        [EMPTY, 'O', 'X'],
        ['X', EMPTY, 'O']]

p = winner(board)
q = terminal(board)

print(result(board,(1,0)))