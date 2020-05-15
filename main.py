#File Made By Thomas Smullen
#Tutorial From https://www.youtube.com/watch?v=XpYz-q1lxu8
#By FreeCodeCamp.org
import numpy as np

#Global Vars
ROW_COUNT = 6
COLLUMN_COUNT = 7
WINNING_CHAIN =4
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

def winningMove(board, piece):
    #Horizontal Locations for winning, check all possible locations where a chain can start
    # and then one directly next to that location, cont.
    for c in range(COLLUMN_COUNT-(WINNING_CHAIN-1)):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #vertical Locations for winning, same as above but increase row instead of col
    for c in range(COLLUMN_COUNT):
        for r in range(ROW_COUNT-(WINNING_CHAIN-1)):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #Positive diag Slopes for winning, increase both row and col
    for c in range(COLLUMN_COUNT-(WINNING_CHAIN-1)):
        for r in range(ROW_COUNT-(WINNING_CHAIN-1)):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #Negative diag slopes for winning, increase col, reduce row
    for c in range(COLLUMN_COUNT-(WINNING_CHAIN-1)):
        for r in range((WINNING_CHAIN-1),ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    #Was attempting to make a check for any value of chains, not just 4, currently not working.
    # for c in range(COLLUMN_COUNT-(WINNING_CHAIN-1)):
    #     for r in range(ROW_COUNT):
    #         for w in range(WINNING_CHAIN):
    #            if board[r][c] == piece and board[r][c+w] == piece and board[r][c+w] == piece and board[r][c+w] == piece:
    #                 return True


            
            
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
            if winningMove(board, 1):
                print("Player 1 Wins")
                gameOver = True
        turn += 1
    

    #P2 Input
    
    elif turn == 1:
        col = int(input("P2, Make Your Selection (0-6)"))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)
            printBoard(board)
            if winningMove(board, 2):
                print("Player 2 Wins")
                gameOver = True
        turn += 1
    elif turn == 2:
        col = int(input("P3, Make Your Selection (0-6)"))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 3)
            printBoard(board)
            if winningMove(board, 3):
                print("Player 3 Wins")
                gameOver = True
        turn = 0