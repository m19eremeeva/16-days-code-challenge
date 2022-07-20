import random
from art import logo
from game_data import data
print(logo)
print('Welcome to higher-lower game! Is this game you have to choose from two Instagram accounts the one with the '
      'most followers.')
if input('Are you ready to start? Type "yes" or "no"\n') == 'yes':
    game_over = False
else:
    game_over = True
    print('Come back when you want to play the game. Bye!')


def exclude_one_item(datas):
    item = random.choice(datas)
    datas.remove(item)
    return item, datas


def compare_two_items(item_a, item_b):
    if item_a['follower_count'] > item_b['follower_count']:
        win_item = item_a
    else:
        win_item = item_b
    return win_item


def one_round(dataset):
    global item_A, count, game_over
    print(
        f'Compare A: {item_A["name"]}, a {item_A["description"]}, from {item_A["country"]}')
    item_b, dataset = exclude_one_item(dataset)
    print('vs')
    print(
        f'Against B: {item_b["name"]}, a {item_b["description"]}, from {item_b["country"]}')
    user_choice = input("Who has more followers? Type 'A' or 'B'\n")
    if user_choice.upper() == 'A':
        user_choice = item_A
    elif user_choice.upper() == 'B':
        user_choice = item_b
    if user_choice != compare_two_items(item_A, item_b):
        game_over = True
        print(f"Sorry, that's wrong. Final score: {count}")
    else:
        count += 1
        print(f"You're right! Current score: {count}")
    item_A = item_b
    return dataset


count = 0

item_A, data = exclude_one_item(data)
while not game_over:
    one_round(data)
