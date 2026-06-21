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
# 7 
number_1 = int(input("what is your number"))
number_2 = int(input("what is your number "))    
if number_1 > number_2:
    print("first is bigger")
elif number_2 > number_1:
    print("second bigger")
else:
    print("equal")    
# 8 
fuel = 40 
distance = 30 
if fuel - distance >=10:
    print("enough fuel with reserve ")
elif 0 < fuel - distance <10 : 
    print("enough fuel,low resaerv ") 
else:
    print("not enough fuel ")