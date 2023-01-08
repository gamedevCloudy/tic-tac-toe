
import random as r

def decideID(playerID,cpuID): 
    playerID= playerID+input("Which one do you want? X/O: ")
    
    if playerID=="X": 
        cpuID+="O"
    elif playerID=="O": cpuID+="X"
    else: 
        print("wrong choice...")
        decideID(playerID,cpuID)
    return (playerID,cpuID)


def printBoard(board): 
    for i in board: 
        print(i,"\n")
    
    print("-"*20,"\n")

def playerMove(playerID, board):
    move = input("Where to place? ")
    move = move.split()
    board[int(move[0])][int(move[1])] = (playerID)
    return board

def cpuMove(cpuID,board):
    move = [0,0]
    move[0]= r.randint(0,2)
    move[1]= r.randint(0,2)
    while(board[move[0]][move[1]] != ""):
        move[0]= r.randint(0,2)
        move[1]= r.randint(0,2)
    board[int(move[0])][int(move[1])] = (cpuID)
    return board

def checkWin(board): 
    for i in board:
        if i[0]==i[1]==i[2] and i[0]!="": return (True, i[0])
 
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!="": return (True,board[0][i])

    if board[0][0]==board[1][1]==board[2][2] and board[2][2]!="": return (True, board[0][0])
    if board[0][2]==board[1][1]==board[2][0] and board[2][0]!="": return (True, board[0][2])

    return False, ""

def main(): 
    #create a 3*3 grid
    rows, cols = (3, 3)
    board = ([["" for i in range(cols)] for j in range(rows)])

    playerID=""
    cpuID=""
    moveCount = 0

    playerID,cpuID=decideID(playerID,cpuID)
    print(*playerID,*cpuID)

    won=False
    while(not won):

        if moveCount>5: 
            won,who= checkWin(board)
            print(won)
            if won== True and who==playerID: 
                print("\nPlayer Won!")
                exit(0)
            elif won== True and who==cpuID: 
                print('\nComputer Won!')
                exit(0)
        
        board=playerMove(playerID,board)
        moveCount+=1
        
        printBoard(board)
        
        board=cpuMove(cpuID,board)
        moveCount+=1
        
        printBoard(board)


main()

