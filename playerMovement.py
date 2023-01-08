def playerMove(playerID, board):
    move = input("Where to place? ")
    move = move.split()

    if  board[int(move[0])][int(move[1])]!= "O" and board[int(move[0])][int(move[1])]!="X": 
        board[int(move[0])][int(move[1])]= (playerID)
        return board
    else:
        print("\nTRY AGAIN!\n") 
        return playerMove(playerID,board)