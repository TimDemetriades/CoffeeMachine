# Coffee Machine - Class Version
# Tim Demetriades
# 6/18/2020

class CoffeeMachine:
    coffee_types = {
                  'espresso':
                            {
                            'water': 250,
                            'beans': 16,
                            'cups': 1,
                            'money': 4    
                            },
                  'latte':
                            {
                            'water': 350,
                            'milk': 75,
                            'beans': 20,
                            'cups': 1,
                            'money': 7    
                            },
                  'cappuccino':
                            {
                            'water': 200,
                            'milk': 100,
                            'beans': 12,
                            'cups': 1,
                            'money': 6    
                            }              
                  }

    def __init__(self, water, milk, beans, cups, money):
        self.water_amount = water
        self.milk_amount = milk
        self.beans_amount = beans
        self.cups_amount = cups
        self.money_amount = money

    def print_amounts(self):
        """
        Prints current values of supplies
        return: none
        """
        print(f"""
The coffe machine has:
{self.water_amount} of water
{self.milk_amount} of milk
{self.beans_amount} of coffee beans
{self.cups_amount} of disposable cups
{self.money_amount} of money
        """)

    def checker(self, amount, amount_per):
        """
        Check how many cups it could make with amount of supplies
        param: amount = current amount
        param: amount_per = amount needed per cup
        return: amount of cups current supply could make
        """
        return amount // amount_per

    def buy(self, choice):
        """
        Lets user buy coffee
        param: choice = type of coffee selected
        return: none
        """
        amount_dict = {}
        if choice == '1':
            amount_dict['water'] = self.checker(self.water_amount, CoffeeMachine.coffee_types['espresso']['water'])
            amount_dict['beans'] = self.checker(self.beans_amount, CoffeeMachine.coffee_types['espresso']['beans']) 
            amount_dict['cups'] = self.checker(self.cups_amount, CoffeeMachine.coffee_types['espresso']['cups'])

            min_amount = min(amount_dict, key=amount_dict.get)          
            min_value = amount_dict[min_amount]

            if min_value == 0:
                print(f'Sorry, not enough {min_amount}!')
                amount_dict.clear()
            else:
                print('I have enough resources, making you a coffee!')
                self.water_amount -= CoffeeMachine.coffee_types['espresso']['water']
                self.beans_amount -= CoffeeMachine.coffee_types['espresso']['beans']
                self.cups_amount -= CoffeeMachine.coffee_types['espresso']['cups']
                self.money_amount += CoffeeMachine.coffee_types['espresso']['money']
                amount_dict.clear()
        if choice == '2':
            amount_dict['water'] = self.checker(self.water_amount, CoffeeMachine.coffee_types['latte']['water'])
            amount_dict['milk'] = self.checker(self.milk_amount, CoffeeMachine.coffee_types['latte']['milk']) 
            amount_dict['beans'] = self.checker(self.beans_amount, CoffeeMachine.coffee_types['latte']['beans']) 
            amount_dict['cups'] = self.checker(self.cups_amount, CoffeeMachine.coffee_types['latte']['cups'])

            min_amount = min(amount_dict, key=amount_dict.get)          
            min_value = amount_dict[min_amount]

            if min_value == 0:
                print(f'Sorry, not enough {min_amount}!')
                amount_dict.clear()
            else:
                print('I have enough resources, making you a coffee!')
                self.water_amount -= CoffeeMachine.coffee_types['latte']['water']
                self.milk_amount -= CoffeeMachine.coffee_types['latte']['milk']
                self.beans_amount -= CoffeeMachine.coffee_types['latte']['beans']
                self.cups_amount -= CoffeeMachine.coffee_types['latte']['cups']
                self.money_amount += CoffeeMachine.coffee_types['latte']['money']
                amount_dict.clear()
        if choice == '3':
            amount_dict['water'] = self.checker(self.water_amount, CoffeeMachine.coffee_types['cappuccino']['water'])
            amount_dict['milk'] = self.checker(self.milk_amount, CoffeeMachine.coffee_types['cappuccino']['milk']) 
            amount_dict['beans'] = self.checker(self.beans_amount, CoffeeMachine.coffee_types['cappuccino']['beans']) 
            amount_dict['cups'] = self.checker(self.cups_amount, CoffeeMachine.coffee_types['cappuccino']['cups'])

            min_amount = min(amount_dict, key=amount_dict.get)          
            min_value = amount_dict[min_amount]

            if min_value == 0:
                print(f'Sorry, not enough {min_amount}!')
                amount_dict.clear()
            else:
                print('I have enough resources, making you a coffee!')
                self.water_amount -= CoffeeMachine.coffee_types['cappuccino']['water']
                self.milk_amount -= CoffeeMachine.coffee_types['cappuccino']['milk']
                self.beans_amount -= CoffeeMachine.coffee_types['cappuccino']['beans']
                self.cups_amount -= CoffeeMachine.coffee_types['cappuccino']['cups']
                self.money_amount += CoffeeMachine.coffee_types['cappuccino']['money']
                amount_dict.clear()

    def fill(self, water, milk, beans, cups):
        """
        Lets user add supplies
        param: water = amount of water to be added
        param: milk = amount of milk to be added
        param: beans = amount of coffee beans to be added
        param: cups = amount of disposable cups to be added
        return: none
        """
        self.water_amount += water
        self.milk_amount += milk
        self.beans_amount += beans
        self.cups_amount += cups

    def take(self):
        """
        Lets user take all money
        return: none
        """
        print(f'I gave you ${self.money_amount}')
        self.money_amount = 0
                
coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)       # Coffee Machine object

# Main loop
while True:
    action = input('Write action (buy, fill, take, remaining, exit): ')
    if action == 'buy':
        while True:
            choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
            if choice == '1' or choice == '2' or choice == '3':
                coffee_machine.buy(choice)
                break
            elif choice == 'back':
                break
            else:
                print('Please enter 1, 2, 3, or back')
                continue
    elif action == 'fill':
        try:
            water = int(input('Write how many ml of water you want to add: '))
            milk = int(input('Write how many ml of milk you want to add: '))
            beans = int(input('Write how many grams of coffee beans you want to add: '))
            cups = int(input('Write how many disposable cups you want to add: '))
        except:
            print('You must enter amounts')
        else:
            coffee_machine.fill(water, milk, beans, cups)
    elif action == 'take':
        coffee_machine.take()
    elif action == 'remaining':
        coffee_machine.print_amounts()
    elif action == 'exit':
        break
    else:
        print('Please enter either buy, fill, or take')