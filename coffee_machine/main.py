import json
import platform
import os
import art


def load_file(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data

class CoffeeMachine:
    def __init__(self, data):
        self.menu = data["Menu"]
        self.resources = data["Resources"]
        self.is_on = True

    def check_resources(self, drink):
        recipe = drink['recipe']
        for resource in recipe.keys():
            if recipe[resource] > self.resources[resource]:
                return False
        return True

    def process_coin(self, coins):
        self.total = round(sum(coins),2)
        return self.total

    def make_coffee(self, drink_name, coins):
        if drink_name not in self.menu:
            print("Sorry drink is not in the menu!")
            return 0
        coins_inserted = self.process_coin(coins=coins)

        drink = self.menu[drink_name]
        if self.check_resources(drink) and coins_inserted >= drink["price"]:
            recipe = drink["recipe"]
            for item in recipe:
                self.resources[item]-=recipe[item]
            change = coins_inserted - drink["price"]
            print(f"Here is your {drink_name}. Enjoy it!")
            print(f"Your change {round(change,2)}")
        else:
            print("Sorry, There are not enough resources for making coffee.\nContact with provider at: (xxx)xxx-xxxx")
            print(f"return ${coins_inserted}")

    def turn_off(self):
        print("Machine Turn Off! Bye-Bye")
        self.is_on = False


    def __str__(self):
        res_status = "\n".join([f"{k} : {v}" for k,v in self.resources.items()])
        return res_status

def clear_console():
    os.system('cls' if platform.system() == "Windows" else 'clear')

if __name__ == "__main__":
    file = "data.json"
    data = load_file(file)
    coffee_machine = CoffeeMachine(data=data)
    
    while coffee_machine.is_on:
        print("Welcome To:")
        print(art.logo)


        drink_name = input("What do you want to drink today?(espresso|latte|cappuccino):\n")

        if drink_name == 'print':
            print(coffee_machine)
            continue

        if drink_name == "off":
            coffee_machine.turn_off()
            continue

        if drink_name not in coffee_machine.menu:
            print("Sorry, that drink its not in the menu")
            continue

        price = coffee_machine.menu[drink_name]['price']
        print(f"{drink_name} price: ${price}\n")
        accept = False
        coins = []
        while not accept:
            try:
                coin = float(input("Insert coins (0.01|0.05|0.10|0.25): "))
                if coin in [0.01,0.05,0.10,0.25]: 
                    coins.append(coin)
                    if price <= sum(coins):
                        accept = True
                else:
                    print("Invalid coin. Please insert valid denominations.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        coffee_machine.make_coffee(drink_name=drink_name, coins=coins)
        restart = input("Do you want to go-back at the main menu? (Y/N)")

        if restart.lower == "y":
            clear_console()
        else:
            coffee_machine.turn_off()