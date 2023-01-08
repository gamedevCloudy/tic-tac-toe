import random as r
def cpuMove(cpuID,board):
    move = [0,0]
    move[0]= r.randint(0,2)
    move[1]= r.randint(0,2)
    while(board[move[0]][move[1]] != ""):
        move[0]= r.randint(0,2)
        move[1]= r.randint(0,2)
    board[int(move[0])][int(move[1])] = (cpuID)
    return board