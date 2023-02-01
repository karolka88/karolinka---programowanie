#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12 or len(username) < 1:
    print("Your username maximum lenght is 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digitals")
else:
    print(f"Welcome {username} :)")