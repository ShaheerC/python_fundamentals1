#Ask the user to enter a number. Use an if statement to print "that's a big number!" if the number is 100 or more, or "why not dream a little bigger?" otherwise.
print("Hello! Please enter a number")
num = input()

if int(num) > 99:
    print("That's a big number!")
elif int(num) < 100:
    print("Why not dream a little bigger?")