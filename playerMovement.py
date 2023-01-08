def playerMove(playerID, board):
    move = input("Where to place? ")
    move = move.split()
    board[int(move[0])][int(move[1])] = (playerID)
    return board