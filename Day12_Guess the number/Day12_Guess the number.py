from art import logo
import random

want_to_play = True
while want_to_play:
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
    hidden_number = random.randint(1, 100)
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    game_over = False


    def one_iteration():
        global lives, game_over
        if lives == 0:
            game_over = True
            return "You've run out of attempts. You lose."
        else:
            print(f"You have {lives} attempts to guess the number")
            user_number = int(input("Make a guess: "))
            if user_number > hidden_number:
                lives -= 1
                return 'Too high!\nGuess again.'
            elif user_number < hidden_number:
                lives -= 1
                return 'Too low!\nGuess again.'
            elif user_number == hidden_number:
                game_over = True
                return f'You got it! The answer was {hidden_number}'


    while not game_over:
        print(one_iteration())

    if input("Do you want to play again? 'yes' or 'no'") == 'no':
        want_to_play = False
