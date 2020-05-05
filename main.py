import numpy as np

#Global Vars
ROW_COUNT = 6
COLLUMN_COUNT = 7
#Create matrix of zeros, WxH of 7,6
def createBoard():
    board = np.zeros((ROW_COUNT,COLLUMN_COUNT))
    return board

board = createBoard()
gameOver = False
turn = 0
#Main Game Loop

while not gameOver:
    #P1 Input
    if turn == 0:
        selection = int(input("P1, Make Your Selection (0-6)"))
        turn += 1
    

    #P2 Input
    else:
        selection = int(input("P2, Make Your Selection (0-6)"))
        turn += 1
        turn = turn % 2