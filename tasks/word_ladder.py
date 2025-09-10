# 7) Word Ladder Game
# What to do:
# - Start with one word (e.g., "cold").
# - Change one letter at a time to reach target word ("warm").
# - Each intermediate step must be a valid word.

# Expected Output:
# Word Ladder: cold → warm
# Enter next word: cord
# Enter next word: word
# Enter next word: ward
# Enter next word: warm
# 🎉 You solved it in 4 steps!



  
def wordladder():
    
    count=0
    user_input=input("enter next word : ")
    for i in user_input:
        if i in op_word:
            count+=1
    if count<=0:
        print("you lose")
        return False
    elif user_input==op_word:
        print(f"you solved it in {steps} steps.")
        return False
    else:
       
        return True

word="cold"
op_word="warm"
steps=1
print(f"Word Ladder : {word}")
while True:
    result=wordladder()
    if result:
        steps+=1
        continue
    else:
        break




