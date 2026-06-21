user_age = int (input("enter your age"))
if user_age >= 18:
    print("can enter ")
else:
    print("cant enter") 
 # number 2 
temperature=35.0 
if temperature >=37.5:
    print("high temperature") 
else:          
    print('normal temperature') 
# 3 
my_number = 7
giveng_number =int(input("what is your number")) 
if my_number==giveng_number: 
    print("even_number")
else: 
    print("odd number ")
   #4 
battery = 15 
is_charging= True 
if battery >20 and is_charging == True:
    print("low battery ,charging now ")
elif battery >20 and is_charging == False :
    print("loe battery , connect charger ")
else:
    print("battery ok ")    
# 5 
passwodr ="python123" 
user_password = input("enter your password")
if passwodr == user_password:
    print("access approved")
else:
    print("acssess denied ")    
# 6 
score = 72
if score > 90:
    print("excellent")
elif score >= 75:
    print("good")
elif score > 60:
    print("pass") 
else:
    print("fail")       