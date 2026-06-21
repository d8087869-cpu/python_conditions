trip = input("where do you want to go ")
match trip:
    case forest: 
        choose = input("where do you want to go , hide or walk ")
        if choose == "hide": 
            print("you hide behind a tree ")
        if choose == "walk": 
            print("you find a sleeping wolf")    