order_price = float(input("enter order price"))
if order_price < 50:
    print("order to small for delivery")
else:
    member = input("are you in the club member ? yes,no:") 
    if member == "yes":
        coupon = input("do you have a coupon? yes,no")
        if coupon == "yes":
            print("free delivery and 10 discount")
        else:
            print("free delivery")    
    else:
        print("delivery costs 15 ")        