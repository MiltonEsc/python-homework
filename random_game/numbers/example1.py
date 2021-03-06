# -*- coding: utf-8 -*-

# Here we're going to make a game where the computer will think of a random number from an interval
# given by the user, and ask (s)he to guess it. The program should tell you if each guess is higher
# or lower. You win if you can guess the number within six tries.

# It is intended to demonstrate a nice variety of concepts seen in class, such as "import", "while"
# and "if" statements; Modules; Conditions; Blocks; Booleans; Comparison operators; "break" keyword;
# the random.randint() function and the "os" module.

# Let's import random to generate pseudo-random numbers
import random
# Let's import OS to use a OS dependent functionality (exit)
import os

# Let's declare some helpful variables
first_number = int(input("Type the initial value:"))
last_number = int(input("Type the last value:"))
random_number = random.randint(first_number, last_number)
tries = 0
tries_remaining = 6
has_won = False

# Functions provide better modularity for our app and good code reusing.

# Here we have a function to make the necessary tests to the user input
# (if it's in the interval, if it's lower or bigger... )
def test_number(guess_num, tries, tries_remaining, has_won):
    if not guess_num > 0 or not guess_num < last_number:
        print "That number isn't in the given interval."
        tries -= 1
        tries_remaining += 1

    elif guess_num == random_number:
        print("Congratulations! You are correct! It took you {} tries.".format(tries))
        has_won = True

    elif guess_num < random_number:
        if tries_remaining > 0:
            print("I'm sorry, that number is low. You have {} tries remaining.".format(int(tries_remaining)))
        else:
            print("You are out of tries. The number was {}".format(random_number))

    elif guess_num > random_number:
        if tries_remaining > 0:
            print("I'm sorry, that number is high. You have {} tries remaining.".format(int(tries_remaining)))
        else:
            print("You are out of tries. The number was {}".format(random_number))
            os.exit()

    return (tries, tries_remaining, has_won)

# Here we have a function to perform the main cicle of the program
def main(random_number, tries, tries_remaining, has_won):
    while tries < 6:
        guess = input("Guess a random number in the given interval:")
        tries += 1
        tries_remaining -= 1

        try:
            guess_num = int(guess)
            tries, tries_remaining, has_won = test_number(guess_num, tries, tries_remaining, has_won)

        except:
            print("That's not a natural number.")
            tries -= 1
            tries_remaining += 1

        if has_won:
            break

main(random_number, tries, tries_remaining, has_won)
