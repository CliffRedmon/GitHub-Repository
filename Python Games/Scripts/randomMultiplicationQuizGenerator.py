#Import random to choose random values
import random

name = input("What is your name? ")

#establish player points
player_points = 0

#creates loop so quiz goes on infinitely
while True:
    x = random.randint(0,9)
    y = random.randint(0,9)
    print("What is " + str(x) + " times " + str(y) + "?")
    answer = int(input("What is your answer: "))
    if answer == (x * y):
        print("Correct!")
        player_points += 1
    else:
        print("Incorrect. The answer is " + str(x*y))
        player_points -= 2
    if player_points < 0:
        player_points = 0
    print(name + " has " + str(player_points) + " points")
    if player_points == 10:
        print('Quiz passed. Thank you for playing.')
        break
