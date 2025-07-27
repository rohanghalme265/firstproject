# Cards games
'''
*The 'war' process can be repeated in this case of back to back ties
*to construct this game,we will create:
      1]. Card Class
      2]. Deck Class
      3]. Player Class
      4]. Game Class
'''

# Step-1

# CARD
# SUIT,RANK,VALUE\
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

two_hearts = Card("Hearts","Two")
print(two_hearts)
print(two_hearts.rank)
print(values[two_hearts.rank])

three_of_clubs = Card("Clubs","Three")
print(three_of_clubs.rank)
print(values[three_of_clubs.rank])

print(three_of_clubs.suit)
print(three_of_clubs.value)

print(two_hearts.value == three_of_clubs)









































































































