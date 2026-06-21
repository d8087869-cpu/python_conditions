correct_pin = 4321
balance = 500 
user_pin = int(input("enter your pin"))
if user_pin == correct_pin:
    amount = int(input("enter withdrawal amount:"))
    if amount > balance:
        print("not enough money ")
        