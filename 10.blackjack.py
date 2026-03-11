import random
from art import black_jack_logo
print(black_jack_logo)
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

user_cards=[]
computer_cards=[]
for _ in range(2):
    deal_card