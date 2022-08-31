from . import card

import random
# from boss import Dealer

class Deck:
    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = {}   #key = value

        for s in suits:  # will loop 4 times
            for i in range(1,14):     #range(start,ending+1) #loop 13 times
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
                self.cards[f"{i},{s}"] = card.Card( s , i , str_val )   #add key/value pairs into the dict

    def show_cards(self):
        for card in self.cards:
            card.card_info()
            
    def pull_card(self, person):
        roll = random.randint(1,13)   #different than range, random.randint is inclusive
        rand_suit = random.randint(1,4)
        if(rand_suit == 1):
            rand_suit = "spade"
        elif(rand_suit == 2):
            rand_suit = "hearts"
        elif(rand_suit == 3):
            rand_suit = "clubs"
        else:
            rand_suit = "diamonds"
        pulled_card = self.cards.pop(f"{roll},{rand_suit}")
        person.cards.append(pulled_card)
        return self
        


class Dealer():
    def __init__(self, name):
        self.name = name
        self.cards =[]



class Player():
    def __init__(self, name, chip = 100):
        self.name = name
        self.cards = []
        self.chip = chip
        
    # def place_chip(self):




# deck1.pull_card(dealer1)
# deck1.pull_card(player1)

# print(dealer1.cards)
# print(player1.cards)




