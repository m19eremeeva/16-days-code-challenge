from info import resources, MENU


def get_report(supplies):
    started_sum = 10
    for keys, values in supplies.items():
        if keys == 'coffee':
            print(keys.capitalize(), values, ' g')
        elif keys != 'money $':
            print(keys.capitalize(), values, ' ml')
        else:
            print(keys.capitalize(), values - started_sum)


def check_resources(drink, supplies, data):
    not_enough = []
    for keys in data[drink]["ingredients"].keys():
        if supplies[keys] < data[drink]["ingredients"][keys]:
            not_enough.append(keys)
    return not_enough


def input_money():
    print("Please insert coins.")
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    return 0.01 * pennies + 0.05 * nickles + 0.1 * dimes + 0.25 * quarters


def update_resources(supplies, drink, data, money):
    supplies['money $'] += money
    for keys in data[drink]["ingredients"].keys():
        supplies[keys] -= data[drink]["ingredients"][keys]


while True:
    user_choice = input('What would you like? (espresso/latte/cappuccino):\n')
    if user_choice == 'off':
        break
    if user_choice == 'report':
        get_report(resources)
    else:
        availability = check_resources(user_choice, resources, MENU)
        if not availability:
            coins = input_money()
            if coins >= MENU[user_choice]['cost']:
                change = coins - MENU[user_choice]['cost']
                if change > resources['money $']:
                    print("The machine doesn't has change for you.")
                else:
                    print(f"Here is ${change} in change.\nHere is your {user_choice} ☕ Enjoy")
                update_resources(resources, user_choice, MENU, MENU[user_choice]['cost'])
            else:
                print('Sorry that is not enough money. Money refunded')
        else:
            print(f"Sorry there is not enough {', '.join(availability)}")
