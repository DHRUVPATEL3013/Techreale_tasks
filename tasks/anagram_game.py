# 5) Word Scramble / Anagram Game
# What to do:
# - Program picks a random word and scrambles letters.
# - Player guesses original word.
# - Track score for multiple rounds.

# Expected Output:
# Scrambled word: "thpyno"
# Your guess: python
# ✅ Correct!
# Next word: "rgpoarm"
# Your guess: program
# ✅ Correct! Score: 2


import random
class AnagramGame():
    def __init__(self):
        self.score=0
        self.words=["python","india","techreale","laptop","rolex"]  
        self.user_guessed=[] 
       
    def start_game(self):
        
        while True:
            self.chosen_word=random.choice(self.words)
            if self.chosen_word in self.user_guessed:
                continue
            else:
                break

        self.scrambled_word=list(self.chosen_word)
        random.shuffle(self.scrambled_word)
        self.scrambled_word="".join(self.scrambled_word)
        print(f"scrambled word : {self.scrambled_word}")
        self.user_input=input("Your Guess : ")

        if self.user_input.lower() == self.chosen_word:
            print("you guessed correct word")
            self.score +=1
            print(f"your Score : {self.score}")
            self.user_guessed.append(self.chosen_word)
            if len(self.user_guessed)==len(self.words):
                print("you won the game")
                return False

            return True
 
        else:
            print("incorrect guess.")
            return False

ang_game=AnagramGame()
is_win=True
while is_win:
    result=ang_game.start_game()
    is_win=result


