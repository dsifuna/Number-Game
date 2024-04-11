import random
import math

#Input 1
lower = int(input("Enter lower range: "))

#Input 2
upper = int(input("Enter upper range: "))

#Random Number Generation
x = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
       " chances to guess the integer!\n")
# Initializing the number of guesses.
count = 0
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # taking guessing number as input
    guess = int(input("Guess a number: "))
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
        

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
    