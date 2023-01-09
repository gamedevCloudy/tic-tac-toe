import random as r
import playerID as pid
pidx=""
def pid(cpuID):
    if cpuID=="X": return "O"
    else: return "X"
def cpuMove(cpuID,board):
    pidx=pid(cpuID)
    row = strategy1(board,pidx)
    print(row)
    
    if row!=None: 
        print("\nGoing for strategy 1..")
        for i in board[row]: 
            if i=="":
                board[row][board[row].index(i)]=(cpuID)
                return board
    else:
        move = [0,0]
        move[0]= r.randint(0,2)
        move[1]= r.randint(0,2)
        while(board[move[0]][move[1]] != ""):
            move[0]= r.randint(0,2)
            move[1]= r.randint(0,2)
        board[int(move[0])][int(move[1])] = (cpuID)
        return board


def strategy1(board,pidx):
    #try to block player's current row
    row = board[0]
    count=0

    for i in board: 
        for j in i:
            if j==pidx:
                count+=1
        if count>=2: 
            row=j
            return board.index(i)
        else: return None
