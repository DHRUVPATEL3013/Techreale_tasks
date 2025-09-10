import random
deck_card=[1,2,3,4,5,6,7,8,9,10,10,10,10]

random.shuffle(deck_card)
shuffled_cards=deck_card
print(deck_card)
print(shuffled_cards)

user_cards=[]
dealer_cards=[]
for i in range(2):
    user_cards.append(shuffled_cards.pop())
    dealer_cards.append(shuffled_cards.pop())

user_total=user_cards[0]+user_cards[1]
dealer_total=dealer_cards[0]+dealer_cards[1]

print(f"your cards : {user_cards} -> total : {user_total}")
print(f"Dealer cards : {[dealer_cards[0],'?']} ")
user_input=input("Hit or Stand : ").lower()

def win_or_lose():

    if user_total>21:
        print(f"user card : {user_cards} Total : {user_total}")
        print(f"dealer card : {dealer_cards} Total : {dealer_total}")
        print("you lose")
    elif user_total > dealer_total:
        print(f"user card : {user_cards} Total : {user_total}")
        print(f"dealer card : {dealer_cards} Total : {dealer_total}")
        print("you win")
    else:
        print(f"user card : {user_cards} Total : {user_total}")
        print(f"dealer card : {dealer_cards} Total : {dealer_total}")
        print("you lose")


if user_input == "hit":
    user_cards.append(shuffled_cards.pop())
    user_total += user_cards[2]
    win_or_lose()
    
else:
    win_or_lose()

        

    