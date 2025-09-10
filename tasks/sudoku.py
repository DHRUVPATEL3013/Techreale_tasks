sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def start_game():
    all_moves=[]
    all_filled=False
    while not all_filled:

        row=int(input("enter row : "))
        column=int(input("enter column : "))
        num=int(input("enter the number"))
        user_input=(row,column)
        
        if user_input not in all_moves and sudoku_board[row][column]>0:
            print("you cant enter here it is already field ")
            for row in sudoku_board:
                print(row)
        
        elif sudoku_board[row][column]==0:
            sudoku_board[row][column]=num
            all_moves.append(user_input)    
            for row in sudoku_board:
                print(row)
        all_rows=[]
        for row in sudoku_board:
            if 0 in row:
                all_rows.append(False)
            else:
                all_rows.append(True)
        if all(all_rows):
            
            all_filled=True
            return all_filled


def rows_check():

    # if result:
        for row in sudoku_board:
            if len(set(row)) <9:
                return {"status":False,"message":"Wrong Solution"}
        else:
            return {"status":True,"message":"Correct Solution"}

def column_check():

    trans_sudoku=[]

    for i in range(len(sudoku_board)):
        l=[]
        for j in range(len(sudoku_board)):
            l.append(sudoku_board[j][i])
        trans_sudoku.append(l)
        
    for row in trans_sudoku:
        if len(set(row) < 9):
            return {"status":False,"message":"Wrong Solution"}
    else:
        return {"status":True,"message":"Correct Solution"}
def sub_matrix_check():
    sub_matrix = []
    for box_row in range(0, 9, 3):        
        for box_col in range(0, 9, 3):    
            matrix = []
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    matrix.append(sudoku_board[r][c])
            sub_matrix.append(matrix)


    for row in sub_matrix:
        if len(set(row)) < 9:
            return {"status":False,"message":"Wrong Solution"}
    else:
        return {"status":True,"message":"Correct Solution"}
        


result=start_game()
is_row_correct=rows_check()
is_col_correct=column_check()
is_sub_mat_correct=sub_matrix_check()

if is_row_correct["status"] and is_col_correct["status"] and is_sub_mat_correct["status"]:
    print(is_row_correct["Message"])
else:
    print(is_row_correct["Message"])
            
    




