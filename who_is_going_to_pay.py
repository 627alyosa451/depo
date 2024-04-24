import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
x = len(names)
pay = random.randint(0, x - 1)
print(f"{names[pay]} is going to buy the meal today!")
