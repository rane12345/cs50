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
    numx=0
    numo=0
    for i in range(len(board)):
        for j in range(len(board[i])):
          if board[i][j]=='X':
            numx+=1
          if board[i][j]=='O':
            numo+=1
    if numx==numo:
        return 'X'
    else:
        return 'O'



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]=='EMPTY':
                act.add((i,j))
    return act



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy=board
    play=player(board)
    copy[action[0]][action[1]]=play
    return copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        for j in range(2):
            if board[i][j]!=board[i][j+1]:
                break
            if j==1 and i==2:
                return board[i][j]
    for i in range(3):
        for j in range(2):
            if board[j][i]!=board[j+1][i]:
                break
            if j==1 and i==2:
                return board[i][j]
    j=0
    for i in range(2):
            if board[i][j]!=board[i+1][j+1]:
                break
            if i==1:
                return board[i][j]
            j=j+1
    j=2
    for i in range(2):
        if board[i][j]!=board[i+1][j-1]:
            break
        if i==1:
            return board[i][j]
        j-=1
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    termi=False
    for i in range(3):
        for j in range(3):
            if board[i][j]=="EMPTY":
                termi=True
                break
        if termi==True:
            break
        elif i==2:
            return True
    f=winner(board)
    if f!=None:
        return True
    else:
        return False




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)=='X':
        return 1
    elif winner(board)=="O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    v=10000
    act=actions(board)
    ans=()
    for i in act:
        x=GetMin(result(board,i))
        if x<=v:
            v=x
            ans=i
    return ans

def GetMax(board):
    v=-10000
    if terminal(board)==True:
        return utility(winner(board))
    act=actions(board)
    for i in act:
        v=max(v,GetMin(result(board,i)))
    return v

def GetMin(board):
    v = 10000
    if terminal(board)==True:
        return utility(winner(board))
    act = actions(board)
    for i in act:
        v = min(v, GetMax(result(board, i)))
    return v