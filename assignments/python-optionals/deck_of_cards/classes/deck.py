import card
import random
# from boss import Dealer

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = {}

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards[f"{i}-{s}"] = card.Card( s , i , str_val )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
            
    def dealer_pull_card(self,dealer):
        roll = random.randint(1,13)
        rand_suit = random.randint(1,4)
        if(rand_suit == 1):
            rand_suit = "spade"
        if(rand_suit == 2):
            rand_suit = "hearts"
        if(rand_suit == 3):
            rand_suit = "clubs"
        if(rand_suit == 4):
            rand_suit = "diamonds"
        pulled_card = self.cards.pop(f"{roll}-{rand_suit}")
        dealer.cards[f"{roll}-{rand_suit}"] = pulled_card
        return self
        
        

class Dealer(Deck):
    def __init__(self, name):
        self.name = name
        self.cards ={}

deck1 = Deck()
dealer1 = Dealer("Alex")

deck1.dealer_pull_card(dealer1)

# print(deck1.cards)
# print(dealer1.cards)


# a=deck1.pull_card()
# b=deck1.pull_card()
# c=deck1.pull_card()
# d=deck1.pull_card()

# print(a,b,c,d)