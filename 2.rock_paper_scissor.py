import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_sign=[rock,paper,scissors]
computer_choice=random.randint(0,1)
user_choice=int(input("Enter your choice: 0 for rock/ 1 for paper/ 2 for scissors: "))
print(f"you chose {hand_sign[user_choice]}")
print(f"computer chose{hand_sign[computer_choice]}")

if user_choice == computer_choice:
    print("it's a draw")
elif user_choice == 1 and computer_choice == 0:
    print("you win")
elif user_choice == 2 and computer_choice == 1:
    print("you win")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
else:
    print("you lose")