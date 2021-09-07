"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730403482"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says... ")
random_message: int = (randint(1, 4))
if random_message == 1:
    print(str("You will meet a new friend soon."))
else:
    if random_message == 2:
        print(str("You will soon acquire a large sum of money."))
    else:
        if random_message == 3:
            print(str("The odds will soon be in your favor."))
        else:
            print(str("You will soon embark on a great adventure."))
print(input("Now go spread positive vibes!"))