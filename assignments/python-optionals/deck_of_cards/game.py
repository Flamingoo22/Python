from classes.deck import Deck, Player, Dealer
from classes.card import Card

deck1 = Deck()

dealer1 = Dealer("Alex")

player1 = Player("Jon")


deck1.pull_card(player1)
# deck1.pull_card(player1)
# deck1.pull_card(player1)

print(deck1.cards)
# print(player1.cards)
# print(player1.cards[0])
a = player1.cards[0]
a.items()
# sum = 0
# for i in range(1, len(player1.cards), 3):
#     print(player1.cards[i])
# # print(sum)