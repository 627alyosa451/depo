import random

def check():
    if attempt > number:
        print("too high")
    if attempt < number:
        print("too low")
    if number == attempt:
        print("U win")

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        print("U've 10 attempts")
        return 10
    else:
        print("U've 5 attempts")
        return 5

print("Welcome to the number guessing game\nI'm thinking of a number between 1 and 100.")

number = random.randint(0,100)
print(number) #hile

heart = difficulty()

#game
while heart != 0:
    attempt = int(input("Make a guess: "))
    check()
    if number == attempt:
        break

    else:
        heart -= 1
        print(f"You have {heart} attempts left")
else:
    print(f"U lose\nIt was {number}")
    
