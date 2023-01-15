def printBoard(board): 
    f=open("board.txt","a")
    f.write("\n")
    
    print("-"*20,"\n")
    
    for i in range(0,len(board)): 
        print(board[i],"\n")
        
        f.writelines(board[i])
        f.write("\n")
    
    f.writelines(str("-"*20))
    
    print("-"*20,"\n")