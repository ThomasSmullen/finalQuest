import numpy as np

#Global Vars
ROW_COUNT = 6
COLLUMN_COUNT = 7

#Functions


#Create matrix of zeros, WxH of 7,6
def createBoard():
    board = np.zeros((ROW_COUNT,COLLUMN_COUNT))
    return board
def dropPiece(board, row, col, piece):
    board[row][col] = piece
#check if the collumn is not completely filled by checking top of collumn
def isValidLocation(board, col):
    return board[ROW_COUNT-1][col] == 0
#check to see what the first open spot is on the board given the collumn, to find the row
def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col]== 0:
            return r
#since NumPy has the top left as the origin for matricies, and gravity exists we flip the board 
# across the x(0) axis

def printBoard(board):
    print(np.flip(board, 0))

board = createBoard()
gameOver = False
turn = 0
#Main Game Loop

while not gameOver:
    #P1 Input
    #Ask player for input in what collumn, then change turn. if turn = 1 going in, then it will be 0 going out
    #and Vice-versa due to modulo function
    if turn == 0:
        col = int(input("P1, Make Your Selection (0-6)"))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
            printBoard(board)
        turn += 1
    

    #P2 Input
    
    else:
        col = int(input("P2, Make Your Selection (0-6)"))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)
            printBoard(board)
        turn += 1
        turn = turn % 2