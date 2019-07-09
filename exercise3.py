#Part One
print("What is your name?")
user_name = input()
print("Hello, {}.".format(user_name))
print("How old are you?")
age = input()
year_born = 2019 - int(age)
print("So {}, you were born in {}".format(user_name, year_born))

#Part Two
secret_password = "please"
print("What's the password?")
password_attempt = input()

correct_or_not = (password_attempt == secret_password)

print("That's {}!".format(correct_or_not))

#Part Three
print("How many cookies have been eaten?")
eaten = input()

remaining_cookies = 12 - int(eaten)

print("There are {} cookies left.".format(remaining_cookies))
