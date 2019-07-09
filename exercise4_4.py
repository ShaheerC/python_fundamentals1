#Pick a number and save it in a variable called secret_number. Ask the user to enter a number. If they enter the secret number, print "You win!". If they are off by 1, print "So close!". Otherwise, print "Try again".
secret_number = 28
print("Hello please enter the secret number!")
user_num = int(input())

if user_num == secret_number:
    print("You win!")
else:
    print("Try again!")

if user_num > secret_number:
    result = user_num - secret_number
else:
    result = secret_number - user_num
if result == 1:
    print("So close!")
