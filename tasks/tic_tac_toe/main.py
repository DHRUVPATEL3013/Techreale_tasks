def read_board():
    board=[]
    for i in range(3):
        rows=[]
        for j in range(3):
            rows.append("__")
        board.append(rows)
    try:
        with open("game.txt", "r") as g:
            for line in g:
                row, col, symbol = line.strip().split(",")
                row, col = int(row) - 1, int(col) - 1
                board[row][col] = symbol
    except FileNotFoundError:
        pass
    return board

def display_board(board):
    for row in board:
        print("   ".join(row))
    print("\n")

def check_winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "__":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "__":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "__":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "__":
        return board[0][2]

    return None
