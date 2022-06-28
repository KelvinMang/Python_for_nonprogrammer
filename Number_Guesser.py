import random
import time
print("Hi, welcome to number guessing game, I am going to pick a number between 1 to 100.")
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
corr_num = random.randint(1,100)
guess_count = 0

while(guess != corr_num):
    guess_count += 1

    if(guess>corr_num):
        print(f"The actual number is lower")
    else:
        print("The actual number is higher")

    guess = int(input("What is your guess again?: "))

print(f"You are correct! It took you {guess_count} to guess it")
