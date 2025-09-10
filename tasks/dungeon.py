# 8) Dungeon Escape Game
# What to do:
# - Create grid-based dungeon.
# - Player moves (N/S/E/W).
# - Random traps, treasures, exit point.
# - Win if player reaches exit alive.

# Expected Output:
# You are in a dark dungeon...
# Options: (N)orth, (S)outh, (E)ast, (W)est
# Move: E
# You found a treasure chest!
# Move: S
# Oh no! You stepped on a trap. HP -20.
# Move: E
# 🎉 You escaped the dungeon!
import random
users_moves=[]
all_moves=[]

def board_generator(row=None,column=None):
    for i in range(1,8):
        for j in range(1,8):
            all_moves.append((i,j))
            if row==i and column==j or (i,j) in users_moves or (i,j)==(1,1) :
                print("+",end=" ")
            else:
                print("_",end=" ")
        print()
def traps_reward_exit():
        
    traps=[]
    while len(traps)<=7:
        traps.append((random.randint(1,7),random.randint(1,7)))
    

    rewards=[]
    while len(rewards)<=7:
        ran_place=(random.randint(1,7),random.randint(1,7))
        if ran_place not in traps:
            rewards.append(ran_place)

    exits=[]

    for i in range(1,8):
        exits.append((i,7))
    exit=random.choice(exits)

    return [rewards,traps,exit]


def game_start(user_position):
   
    user_move=input("enter your move (S/E/N/W)").upper()
    
    if user_move=="S":
        user_position=(user_position[0]+1,user_position[1])
    elif user_move=="E":
        print("hello")
        user_position=(user_position[0],user_position[1]+1)
    elif user_move=="N":
        user_position=(user_position[0]-1,user_position[1])
    elif user_move=="W":
        user_position=(user_position[0],user_position[1]-1)
    return user_position

def declare_winner(result,tre):
    HP=100
    if HP<=0:
        print("you lose your Hp is 0")
        return True
    if result == tre[2]:
        print("you won")
        return True
    elif result in tre[0]:
        HP=HP-10
        print("you lose your HP")
    elif result in tre[1]:
        print("you found a tresure")
    elif result in all_moves:
        pass
    else:
        print("invalid move")

tre=traps_reward_exit()
board_generator()
print(tre)
user_position=(1,1)
is_win=False
while not is_win:
    
    result=game_start(user_position)
    user_position=result
    users_moves.append(result)
    board_generator(result[0],result[1])
    print(result)
    win=declare_winner(result,tre)
    if win:
        is_win=True

  
