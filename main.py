#File Made By Thomas Smullen
#Tutorial From https://www.youtube.com/watch?v=XpYz-q1lxu8
#By FreeCodeCamp.org
import numpy as np

#Global Vars
ROW_COUNT = 6
COLLUMN_COUNT = 7
WINNING_CHAIN = 4
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

#Ask player for input, use all functions to determine the next boardstate

def playerTurn(board,player):
    col = int(input("P"+str(player) + " Make Your Selection (0-" + str(COLLUMN_COUNT-1)+")"))
    if isValidLocation(board, col):
        row = getNextOpenRow(board, col)
        dropPiece(board, row, col, player)
        printBoard(board)
        if winningMove(board, player):
            print("Player" + str(player) + "Wins")
            gameOver = True
            

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
    #Call function for player turn with the player number
    if turn == 0:
        playerTurn(board,1)
        if gameOver:
            break
        else:
            turn += 1
 #P2 Input
    
    if turn == 1:
        playerTurn(board, 2)
        turn = 0