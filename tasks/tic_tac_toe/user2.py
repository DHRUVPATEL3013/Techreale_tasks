import time
from main import read_board, display_board, check_winner

while True:
    
    with open("turn.txt", "r") as t:
        turn = t.read().strip()

    if turn != "2":
        time.sleep(1)
        continue

    board = read_board()
    display_board(board)

    row = int(input("User2 - Enter row (1-3): "))
    col = int(input("User2 - Enter col (1-3): "))
    move = f"{row},{col},O\n"
    
    with open("game.txt", "a") as g:
        g.write(move)
    
    board = read_board()
    display_board(board)

    
    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins!")
        break

    with open("turn.txt", "w") as t:
        t.write("1")
