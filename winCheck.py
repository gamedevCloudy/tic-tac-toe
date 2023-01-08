def checkWin(board): 
    for i in board:
        if i[0]==i[1]==i[2] and i[0]!="": return (True, i[0])
 
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!="": return (True,board[0][i])

    if board[0][0]==board[1][1]==board[2][2] and board[2][2]!="": return (True, board[0][0])
    if board[0][2]==board[1][1]==board[2][0] and board[2][0]!="": return (True, board[0][2])

    return False, ""