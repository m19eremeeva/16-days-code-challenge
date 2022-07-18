import random
import replit
from art import logo

print(logo)


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


want_to_play = True
while want_to_play:
    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)


    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if user_score == 0 or user_score > 21 or computer_score == 0:
            game_over = True
        else:
            print(f"Your cards is {user_cards} with total score {user_score}")
            print(f"The opponent's first card is {computer_cards}")
            user_choice = input("Do you want to draw another card? Type 'yes' or 'no' \n")
            if user_choice == 'yes':
                user_cards.append(deal_card())
            elif user_choice == 'no':
                game_over = True
    computer_finish = False
    while not computer_finish:
        computer_score = calculate_score(computer_cards)
        if computer_score < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            if computer_score > 21:
                computer_cards = computer_cards[:len(computer_cards)]
                computer_finish = True
        else:
            computer_finish = True


    def compare(computer_score, user_score):
        if user_score > 21 and computer_score > 21:
            return "You went over. You lose"
        if computer_score == user_score:
            return "You have a draw"
        elif computer_score == 0:
            return "You lose. Your opponent have a Blackjack!"
        elif user_score == 0:
            return "You win. You have a Blackjack!"
        elif user_score > 21:
            return "You lose. You took too many cards!"
        elif computer_score > 21:
            return "You win. Opponent took too many cards"

        elif user_score < computer_score:
            return "You lose. Your opponent have a higher score!"
        elif computer_score < user_score:
            return "You win. You have a higher score!"


    print(
        f"Your cards is {user_cards} with a score: {user_score} \nThe opponent's cards is {computer_cards} with a score:{computer_score}")
    print(compare(computer_score, user_score))

    if input("Do you want to play again? Type 'yes' to restart the game or 'no' to finish the game\n") == 'yes':
        replit.clear()
    else:
        want_to_play = False
