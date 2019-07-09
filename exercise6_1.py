home_km = 0

while True:
    print("Would you like to walk or run?")
    walk_run = input()
    if walk_run == "walk":
        home_km+=1
        print("Distance from home is {} km.".format(home_km))
    elif walk_run == "run":
        home_km+=5
        print("Distance from home is {} km.".format(home_km))
    elif walk_run == "go home":
        print("You have decided to go home.")
        break
    else:
        print("Please enter valid commands only.")