import math
import time
import random
import threading 

users_guess = int(input("Guess a number between 1 and 6 in dice: "))
print("Rolling the dice...")
winning_points = 0
time.sleep(2)
results = [1,2,3,4,5,6]
random_number = random.choice(results)
if users_guess > 6 or users_guess < 1 :
    print("Number is not between 1 and 6")
else:
    if random_number == users_guess:
        print("You win")
        print("The number is: ", random_number)
        winning_points += 1
        print("Your score is: ", winning_points)
    else:
        print("You lose")