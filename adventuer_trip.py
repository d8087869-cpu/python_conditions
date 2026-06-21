trip = input("where do you want to go ")
match trip:
    case "forest": 
        choose = input("where do you want to go , hide or walk ")
        if choose == "hide": 
            print("you hide behind a tree ")
        elif choose == "walk": 
            print("you find a sleeping wolf")    
        else:
            print("invalid forest action")
    case "cave": 
        choose = input("do you have a torch ")      
        if choose == "yes":
            turn = input("left or rigth ")
            if turn == "left":
                print("you find gold ")
            elif turn == "rigth": 
                print("you find bats")
            else:
                print("invalid cave path")  
        else:
            print("its to dark to enter")             
    case "river":
        print("you find a boat")
    case _:
        print("unknown place")
