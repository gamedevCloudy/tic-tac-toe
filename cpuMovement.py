import random as r
import playerID as pid
pidx=''

def pid(cpuID):
    if cpuID=='X': return 'O'
    else: return 'X'

def cpuMove(cpuID,board):
    pidx=pid(cpuID)
    row = strategy1(board,pidx)

    row2,col2 = strategy2(board,pidx)
    
    if row>=0: 
        
        print("Strategy: 1")
        for i in range(0,len(board)-1):
            if board[row][i]=='': 
                board[row][i]=cpuID
                return board

    elif row2 >=0:
        print("Strategy 2: ", row2, col2 )
        board[row2][col2]=(cpuID)
        return board
    else: 
        print("Random Move")
        row2=r.randint(0,2)
        col2=r.randint(0,2)
        while(board[row2][col2] != ''):
            row2=r.randint(0,2)
            col2=r.randint(0,2)
        board[row2][col2]=cpuID
        return board


def strategy1(board,pidx):
    #try to block player's current row
    count=0

    for i in board: 
        for j in i:
            if j==pidx:
                print(i,j)
                count+=1
        if count>=2: 
            print(i,j)
            return board.index(i)
        count=0
    print(-1)
    return -1

def strategy2(board,pidx):
    #try to block player's column
    for i in range(len(board)):
        if board[0][i]==board[1][i]==pidx and board[2][i]!='':
            return 2,i
        elif board[0][i]==board[2][i==pidx] and board[1][i]!='':
            return 1,i
        elif board[1][i]==board[2][i]==pidx and board[0][i]!='':
            return 0,i
    return -1,-1