my_age = 28
print("Hello! Please enter your age.")
user_age = int(input())

if int(user_age) > 104:
    print("I'm not sure I believe you.")
else:
    if user_age > my_age:
        result = user_age - my_age
    else:
        result = my_age - user_age
    print("So we are {}, years apart in age.".format(result))

