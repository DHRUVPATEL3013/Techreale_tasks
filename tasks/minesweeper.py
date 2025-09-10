
import random
def board_generator():
    for i in range(1,6):
        for j in range(1,6):
            print("?",end=" ")
        print()
board_generator()

total_bombs=random.randint(1,10)
print(total_bombs)
placed_bombs=[]
placed=0
while placed < total_bombs:

    row=random.randint(1,5)
    column=random.randint(1,5)
    bomb=(row,column)
    placed_bombs.append(bomb)
    placed+=1

print(placed_bombs)
bomb_found=False

while not bomb_found:
        
    user_row=int(input("enter row"))
    user_column=int(input("enter column"))
    user_input=(user_row,user_column)

    nearby_bombs_possibility=[]

    for i in range(user_input[0]-1,user_input[0]+2):
        for j in range(user_input[1]-1,user_input[1]+2):
            nearby_bombs_possibility.append((i,j))
    # print(nearby_bombs_possibility)

    nearby_bombs=[]
    if user_input in placed_bombs:
        print("Boom ! Game Over")
        bomb_found=True
    else:
        for bomb in placed_bombs:
            if bomb in nearby_bombs_possibility:
                nearby_bombs.append(bomb)
        print(f"nearby bombs : {len(nearby_bombs)}")








