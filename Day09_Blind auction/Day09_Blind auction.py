import replit
import art


print(art.logo)
not_end_of_bid = True
list_of_rates = {}
while not_end_of_bid:
    name = input('What is your name?\n')
    bid = int(input('What is your bid? $\n'))
    list_of_rates[name] = bid
    if input('Is there are other users who want to bid? yes or no\n') == 'no':
        not_end_of_bid = False
    else:
        replit.clear()
winner_bid = max(list_of_rates.values())
for names in list_of_rates:
    if list_of_rates[names] == winner_bid:
        winner = names
print(f'The winner is {winner} with a bid of $ {winner_bid}')