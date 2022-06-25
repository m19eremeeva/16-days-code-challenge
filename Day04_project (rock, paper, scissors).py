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
import random
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
signs = [rock, paper, scissors]
computer = random.randint(0,2)
print(signs[user])
print('Computer chose:')
print(signs[computer])
if user == computer:
    print('You have a draw.')
elif user == 0 and computer == 1:
    print('You lose')
elif user ==0 and computer == 2:
    print('You win')
elif user ==1 and computer == 0:
    print('You win')
elif user ==1 and computer == 2:
    print('You lose')
elif user == 2 and computer == 0:
    print('You lose')
elif user == 2 and computer == 1:
    print('You win')