#TODO:1 Print current status of resources
#TODO:2 Are there sufficient resources for the request of the user?
#TODO:3 Process coins inserted (4 types!)
#TODO:4 Was the transaction successfull?
#TODO:5 Make coffee and update resources
#☕

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

money_in_machine=0

#START HERE

def check_if_enough(order_ingredients):
  """This function returns True if the ingredients are sufficient to make the users request, and False if there are not enough resources (Water, Milk, etc.)"""
  is_enough=True
  for item in order_ingredients:
    if order_ingredients[item]>=resources[item]:
      print(f"Not enough {item}." )
      is_enough=False
  return is_enough


def coin_processer():
  """This function returns the total value of the coins inserted"""
  print("Please insert coins")
  pennies= float(input("How many pennies? "))*0.01
  nickles= float(input("How many nickles? "))*0.05 
  dimes=float(input("How many dimes? "))*0.1
  quarters=float(input("How many quarters? "))*0.25 
  total=float(pennies+nickles+dimes+quarters)
  return total

def update_stock(drink_name,order_ingredients):
  """This function will update the quantity of the ingredients left after serving a customer"""
  for item in order_ingredients:
    resources[item]-=order_ingredients[item]




def start():
  money_in_machine=0
  finished=False
  while not finished:
    user_wish= input("What would you like? (espresso/latte/cappuccino): \nTo turn off the machine just press the 'off' button! ").strip().lower()
    if user_wish=="off":
      finished=True
    elif user_wish=="report":
      print(f"Water: {resources['water']} ml,")
      print(f"Milk: {resources['milk']} ml,")
      print(f"Coffee: {resources['coffee']} g")
      print(f"Money: ${money_in_machine}")
    else:
      drink=MENU[user_wish]
      if check_if_enough(drink["ingredients"])==True :
        payment=coin_processer()
        if payment == drink["cost"]:
          money_in_machine+=payment
          update_stock(user_wish,drink["ingredients"])
          print(f"Enjoy your {user_wish}☕!")
        elif payment> drink["cost"]:
          print(f"Here is ${round(payment-drink['cost'],2)} change. ")
        else:
          print("Sorry that's not enough money. Money refunded. ")


start()
