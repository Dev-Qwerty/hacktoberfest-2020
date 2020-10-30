#  program to shuffle a deck of cards

# importing modules
import itertools, random

# create the deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle
random.shuffle(deck)

# to draw six cards
print("You got:")
for i in range(6):
   print(deck[i][0], "of", deck[i][1])
