import playerID as pID
import winCheck as wc
import playerMovement as pmv
import cpuMovement as cmv
import display as disp

def main(): 
    #create a 3*3 grid
    rows, cols = (3, 3)
    board = ([["" for i in range(cols)] for j in range(rows)])

    playerID=""
    cpuID=""
    moveCount = 0

    playerID,cpuID=pID.decideID(playerID,cpuID)
    print(*playerID,*cpuID)

    won=False
    while(not won):

        if moveCount>5: 
            wc.checkWinner(board,moveCount,playerID,cpuID)

        board=pmv.playerMove(playerID,board)
        moveCount+=1
   
        disp.printBoard(board)
        if moveCount>=9: 
            print("TIE")
            exit()
        
        if moveCount>5: 
            wc.checkWinner(board,moveCount,playerID,cpuID)
        board=cmv.cpuMove(cpuID,board)
        moveCount+=1

        print("\nCPU MOVE\n")
        disp.printBoard(board)

main()