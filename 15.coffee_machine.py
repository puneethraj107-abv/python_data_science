#Coffee Machine Program Requirements
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
total = 0

def resource_sufficient(order_taken):
    for item in order_taken:
        if resources[item]<=order_taken[item]:
            print(f"you have insufficient ingredients")
            return False
        return True
    
def process_coin():
    global total
    total=int(input("please insert quaters: "))*0.25
    total+=int(input("please insert dimes: "))*0.15
    total+=int(input("please insert nickle: "))*0.1
    total+=int(input("pleaser insert pennies: "))*0.05
    return total

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your drink {drink_name}")

profit=0
machine_operation=True

while machine_operation:
    order=input("What would you like? (espresso/latte/cappuccino): ")

    if order=='off':
        print('Turning of the machine')
        machine_operation=False

    elif order == 'report':
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} g")
        print(f"you made ${profit}")
    else:
        drink=MENU[order]['ingredients']
        drink_cost=MENU[order]['cost']
        if resource_sufficient(drink):
            if process_coin()>=MENU[order]['cost']:
                make_coffee(order,drink)
                cash=total
                
                change=cash-drink_cost
                
                profit+=drink_cost
                print(f"here is your change {change}")