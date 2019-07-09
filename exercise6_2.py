home_km = 0
energy = 10

while True:
    print("Would you like to walk or run?")
    walk_run = input()
    
    if walk_run == "walk":
        home_km+=1
        energy+=1
        print("Distance from home is {} km., and you have {} energy left.".format(home_km , energy))
    elif walk_run == "run":
        if energy >= 2:
            home_km+=5
            energy-=2
            print("Distance from home is {} km., and you have {} energy left.".format(home_km , energy))
        else:
            print("Your energy is too low to run")    
    elif walk_run == "go home":
        print("You have decided to go home.")
        break
    else:
        print("Please enter valid commands only.")