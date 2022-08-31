from deck import Deck
# import card
# import random

class Dealer(Deck):
    def __init__(self, name):
        self.name = name
        self.cards ={}
        
    # def pull_card(self):
    #     super().pull_card()
    #     self.cards[f"{roll}-{rand_suit}"] = pulled_card
    #     return self


# dealer1 = Dealer("Alex")

# dealer1.pull_card()