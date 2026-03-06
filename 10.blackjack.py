import random
from art import black_jack_logo
def dealcards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score, c_score):
    if c_score==u_score:
        return "it's a draw"
    elif c_score ==0:
        return "dealer has a blackjack, you lose"
    elif u_score==0:
        return "congradulations you win"
    elif u_score>21:
        return "you lose"
    elif c_score>21:
        return "congadulations, you win"
    elif u_score>c_score:
        return "you win"
    else:
        return "you lose"
def play_game():
    print(black_jack_logo)
    usercards=[]
    computercards=[]
    user_score=-1
    computer_score=-1

    game_over=False
    for _ in range(2):
        usercards.append(dealcards())
        computercards.append(dealcards())

    while not game_over:
        user_score=calculate_score(usercards)
        computer_score=calculate_score(computercards)
        print(f"you're cards{usercards}, and current score is {user_score}")
        print(f"dealers cards {computercards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            user_should_deal=input("do you want to continue,press (y) to continue,(n) to pass: ").lower()
            if user_should_deal == "y":
                usercards.append(dealcards())
            else:
                game_over=True

    while computer_score!=0 and computer_score<17:
        computercards.append(dealcards())
        computer_score=calculate_score(computercards)

    print(f"your final hand {usercards}, and score {user_score}")
    print(f"dealers final hand {computercards}, and score {computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play a game of blackjack,(y) to continue\n")=="y":
    print("\n"*30)
    play_game()