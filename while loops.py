#while loop = execute some code WHILE some condition remains true

# 1.

#name = input("Enter your name: ")

#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your name: ")
#print(f"Hello {name}")

# 2.

#age = int(input("Enter your age: "))

#while age < 0:
#    print("Age can't be negative")
#    age = int(input("Enter your age: "))

#print(f"You are {age} years old")

# 3.

#food = input("Enter your favourite food (q to quit): ")

#while not food == "q":
#    print(f"You like {food}")
#    food = input("Enter another food you like(q to quit): ")

#print("bye")

# 4.

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")