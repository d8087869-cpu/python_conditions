correct_pin = 4321
balance = 500 
user_pin = int(input("enter your pin"))
if user_pin == correct_pin:
    amount = int(input("enter withdrawal amount:"))
    if amount > balance:
        print("not enough money ")
    else:
        receipt = input("do you want a recepit , yes /no")
        match receipt:
            case "yes":
                print("withdrawal with receipt")
            case "no":
                print("withdrawal without receipt")
            case _:
                print("withdrawal approved")        
else :
    print("worng pin")                