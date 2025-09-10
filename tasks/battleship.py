import random
def board_generator(row=None,column=None):
    for i in range(1,6):
        for j in range(1,6):
            if row and column and row==i and column==j:
                    print("*",end=" ")
            else:
                print("~",end=" ")
        print()

def game_start():
    correct_row=False
    while not correct_row:
        
        try:
            row=int(input("enter row (1-5) : "))
            if row>5 or row<=0 :
                print("please select the row between 1 and 5")
            else:
                correct_row=True
        except ValueError:
            print("you can not enter character or string.")
            print("please choose the row beetwen 0 and 5")
      

    correct_column=False
    while not correct_column:
        
        try:
            column=int(input("enter column (1-5) : "))
            if column>5 or column<=0:
                print("please select the column between 1 and 5")
            
            else:
                correct_column=True
        except ValueError as err:
            print("you can not enter character or string.")
            print("please choose the column beetwen 0 and 5")
      
    user_input=(row,column)
    
    if random_ship==user_input:
        return {"row":row,"column":column,"message":"Hit ! you shunk the ship"}
        
    else:
        return None


board_generator()
random_ship=(random.randint(1,5),random.randint(1,5))
print(random_ship)

is_win=False
while not is_win:
    result=game_start()

    if result:
        board_generator(result["row"],result["column"])
        print(result["message"])
        is_win=True
    else:
        print("Miss!")

    
