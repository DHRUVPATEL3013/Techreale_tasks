import random

class Poker:
    def __init__(self):
        self.cards = ['♣A', '♥A', '♦A', '♠A', '♣2', '♥2', '♦2', '♠2', '♣3', '♥3', '♦3', '♠3', '♣4', '♥4', '♦4', '♠4', 
                 '♣5', '♥5', '♦5', '♠5', '♣6', '♥6', '♦6', '♠6', '♣7', '♥7', '♦7', '♠7', '♣8', '♥8', '♦8', '♠8', 
                 '♣9', '♥9', '♦9', '♠9', '♣10', '♥10', '♦10', '♠10', '♣J', '♥J', '♦J', '♠J', '♣Q', '♥Q', '♦Q', '♠Q', 
                 '♣K', '♥K', '♦K', '♠K']
        self.user_hand=[]
        self.dealer_hand=[]
        
    def cards_generator(self):

        random.shuffle(self.cards)
        self.shuffle_cards=self.cards
        
        for i in range(5):
            self.user_hand.append(self.shuffle_cards.pop())
            self.dealer_hand.append(self.shuffle_cards.pop())
        return {"user hand":self.user_hand,"dealer hand":self.dealer_hand}
    
        

    def user_pair_ckeck(self,user_hand):
        self.user_pair=[]
        for card in user_hand:
            for crd in user_hand[user_hand.index(card)+1:]:
            
                if card[1:]==crd[1:]:

                    self.user_pair.append((card,crd))
                
        return {"status": True if len(self.user_pair)>0 else False ,"data":self.user_pair}

    # for user flush
    def user_flush_check(self,user_hand):
        
        self.user_flush=[]
        for card in user_hand:
            if card[0] not in self.user_flush:
                self.user_flush.append(card[0])
            
            
        if len(self.user_flush) == 1:
            return True
        else:
            return False
    
        

    # user straight
    def user_straight_check(self,user_hand):
        self.num=[]
        
        str_cards={"A":1,"K":13,"Q":12,"J":11}
        
        for card in user_hand:
            try:
            # if type(card[1:]) == str:
                self.num.append(str_cards[card[1:]])
            except KeyError:
                self.num.append(int(card[1:]))
            
                
        self.sorted_cards=sorted(set(self.num))
        if self.sorted_cards==[1,10,11,12,13]:
            return self.sorted_cards
        elif len(self.sorted_cards)==5:
            if all(self.sorted_cards[0]+i in self.num for i in range(1,5)):
                return self.sorted_cards
            else:
                return False
        else :
            return False



    def winner(self,hand_card):
        self.flush=self.user_flush_check(hand_card)
        self.straight=self.user_straight_check(hand_card)
        self.pair=self.user_pair_ckeck(hand_card)

        if self.flush and self.straight:
            return {"score":5,"cards":hand_card}
        elif self.flush:
            return {"score":3,"cards":hand_card}
        elif self.straight:

            return {"score":2,"cards":hand_card}
        elif self.pair["status"]:
            return {"score":len(self.pair),"cards":self.pair["data"]}
        
    
        else:
            return {"score":0,"cards":hand_card}
        
    def get_high_card(self,hand):
        self.str_cards={"A":14,"K":13,"Q":12,"J":11}
        self.values=[]
        for card in hand:
            try:
                self.values.append(self.str_cards[card[1:]])
            except KeyError:
                self.values.append(int(card[1:]))
        self.best=max(self.values)
        self.best_card=[]
        for card in hand:
            try:
                if int(card[1:])==self.best:
                    self.best_card.append(card)
            except ValueError:
                if self.best in self.str_cards.values():
                    self.best_card.append(card)



        return self.best_card
    
    def declare_winner(self):


        print(f"user hand  : {self.user_hand}")
        print(f"dealer hand : {self.dealer_hand}")

        self.user_score=self.winner(self.user_hand)
        self.dealer_score=self.winner(self.dealer_hand)

        if self.user_score["score"]==0 and self.dealer_score["score"]==0:
            self.user_result=self.get_high_card(self.user_hand)
            self.dealer_result=self.get_high_card(self.dealer_hand)
            print(self.user_result)
            print(self.dealer_result)
            if self.user_result>self.dealer_result:
                print(f"user best hand : {self.user_result}")
                print("user wins")
            elif self.user_result==self.dealer_result:
                print(f"user best hand : {self.user_result}")
                print(f"dealer best hand : {self.dealer_result}")
                print("draw")
            else:
                print(f"dealer best hand : {self.dealer_result}")
                print("dealer wins")
        elif self.user_score["score"]==self.dealer_score["score"]:
            print(f"User Besthand : {self.user_score['cards']}")
            print(f"Dealer Best Hand : {self.dealer_score['cards']}")

            print("Draw")
        elif self.user_score["score"] > self.dealer_score["score"]:
            print(f"User Besthand : {self.user_score['cards']}")
            print("user win")
        else:
            print(f"Dealer Best Hand : {self.dealer_score['cards']}")
            print("dealer win")


poker=Poker()
poker.cards_generator()
poker.declare_winner()

