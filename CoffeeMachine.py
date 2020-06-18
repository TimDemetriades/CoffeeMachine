# Coffee Machine
# Tim Demetriades
# 6/12/2020

# Initial amounts
water_amount = 400
milk_amount = 540
beans_amount = 120
cups_amount = 9
money_amount = 550

amount_dict = {}

def print_amounts():
    """
    Prints current values of supplies
    return: none
    """
    print(f"""
The coffe machine has:
{water_amount} of water
{milk_amount} of milk
{beans_amount} of coffee beans
{cups_amount} of disposable cups
{money_amount} of money
    """)

def checker(amount, amount_per):
    """
    Check how many cups it could make with amount of supplies
    param: amount = current amount
    param: amount_per = amount needed per cup
    return: amount of cups current supply could make
    """
    return amount // amount_per     

def buy():
    """
    Lets user buy coffee
    return: none
    """
    global water_amount, milk_amount, beans_amount, cups_amount, money_amount

    while True:
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ') 
        if choice == '1':
            amount_dict['water'] = checker(water_amount, 250)   # 250 ml water = 1 cup
            amount_dict['beans'] = checker(beans_amount, 16)    # 16 g beans = 1 cup
            amount_dict['cups'] = checker(cups_amount, 1)
  
            min_amount = min(amount_dict, key=amount_dict.get)          
            min_value = amount_dict[min_amount]                 

            if min_value == 0:
                print(f'Sorry, not enough {min_amount}!')
                amount_dict.clear()
                break
            else:
                print('I have enough resources, making you a coffee!')
                water_amount -= 250
                beans_amount -= 16
                cups_amount -= 1
                money_amount += 4
                amount_dict.clear()
                break
        elif choice == '2':
            amount_dict['water'] = checker(water_amount, 350)   # 350 ml water = 1 cup
            amount_dict['milk'] = checker(milk_amount, 75)     # 75 ml milk = 1 cup
            amount_dict['beans'] = checker(beans_amount, 20)    # 20 g beans = 1 cup
            amount_dict['cups'] = checker(cups_amount, 1)
  
            min_amount = min(amount_dict, key=amount_dict.get)          
            min_value = amount_dict[min_amount]

            if min_value == 0:
                print(f'Sorry, not enough {min_amount}!')
                amount_dict.clear()
                break
            else:
                print('I have enough resources, making you a coffee!')
                water_amount -= 350
                milk_amount -= 75
                beans_amount -= 20
                cups_amount -= 1
                money_amount += 7
                amount_dict.clear()
                break
        elif choice == '3':
            amount_dict['water'] = checker(water_amount, 200)   # 200 ml water = 1 cup
            amount_dict['milk'] = checker(milk_amount, 100)    # 100 ml milk = 1 cup
            amount_dict['beans'] = checker(beans_amount, 12)    # 12 g beans = 1 cup
            amount_dict['cups'] = checker(cups_amount, 1)
  
            min_amount = min(amount_dict, key=amount_dict.get)          
            min_value = amount_dict[min_amount]

            if min_value < 1:
                print(f'Sorry, not enough {min_amount}!')
                amount_dict.clear()
                break
            else:
                print('I have enough resources, making you a coffee!')
                water_amount -= 200
                milk_amount -= 100
                beans_amount -= 12
                cups_amount -= 1
                money_amount += 6
                break
        elif choice == 'back':
            break
        else:
            print("Please enter 1, 2, 3, or back")
            continue

def fill():
    """
    Lets user add supplies
    return: none
    """
    global water_amount, milk_amount, beans_amount, cups_amount

    water_amount += int(input('Write how many ml of water you want to add: '))
    milk_amount += int(input('Write how many ml of milk you want to add: '))
    beans_amount += int(input('Write how many grams of coffee beans you want to add: '))
    cups_amount += int(input('Write how many disposable cups of coffee you want to add: '))

def take():
    """
    Lets user take all money
    """
    global money_amount
    print(f'I gave you ${money_amount}')
    money_amount = 0


# Main Loop
while True:
    action = input('Write action (buy, fill, take, remaining, exit): ')
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        print_amounts()
    elif action == 'exit':
        break
    else:
        print('Please enter either buy, fill, or take')
