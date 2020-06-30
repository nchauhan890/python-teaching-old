"""Notes on while loop exercise."""

# Notes:

# This exercise recommends the use of random numbers
# as the 'random' built-in module in Python allows users
# to generate (pseudo-)random numbers.

import random           # type this at the top of the script
                        # to use this module
random.randint(1, 100)  # this will pick a number in the range
                        # 1 -> 100 (inclusive)

# However, the value generated needs to be assigned to a
# variable so that it can be used more than once. Choose
# a suitable variable name to remember what it represents:

random_num = random.randint(1, 100)
# Do not use names used by anything else which includes
# reserved Python keywords like 'print' and 'import' and
# names from modules - in this case 'random'.



# Approach:

# Start off by setting up your script: import 'random' module
# and create variables needed:
import random
random_num = random.randint(1, 100)
guess = 0  # Will be changed below...

# Now consider how you are going to get user input and how it
# will be handled:
guess = input('Enter your guess: ')

# Remember that the variable 'random_num' is an integer type
# and the input() function automatically returns a string, so
# it needs to be cast into an integer:
guess = int(input('Enter your guess: '))

# Note that I, personally, do not recommend using a bare
# int(input()) as an input that cannot be converted into an
# integer will raise a ValueError and the program will end.
# However, for simplicity, I shall leave it be.

# After you get your input, you need to compare it to the
# 'random_num' variable. If the guess is correct, we need to
# tell the user this:
if guess == random_num:
    print('Correct!')

# If the guess isn't correct, then we'll need to ask for another
# input. Since we've already used that code above, we can add it
# to a while loop:
while True:  # I'll change this later...
    guess = int(input('Enter your guess: '))
    if guess == random_num:
        print('Correct!')

# Here you can edit the 'True' statement in the while loop and
# replace it with the condition in the 'if' statement, but invert
# it. ('==' becomes '!='). Thus, when the guess is wrong, it will
# keep asking for a new answer, but when it is correct, the while
# loop will terminate and 'Correct!' will be printed:
while guess != random_num:
    guess = int(input('Enter your guess: '))
print('Correct!')

# A small caveat here is that the 'guess' variable needs to be
# assigned before the while loop so that it can be used in the
# comparison, else a NameError will be raised.



# Solutions:

# My solution to the original task:

import random
random_num = random.randint(1, 100)
guess = int(input('Enter your guess: '))
while guess != random_num:
    guess = int(input('Enter your guess: '))
print('Correct!')


# My solution to extension 1:

# ...before while loop...
while guess != random_num:
    if guess < random_num:
        print('Guess higher!')
    else:
        print('Guess lower!')
    guess = int(input('Enter your guess: '))
# ...rest of code...


# My solution to extension 2:

import random
while True:
    random_num = random.randint(1, 100)
    guess = int(input('Enter your guess: '))
    while guess != random_num:
        guess = int(input('Enter your guess: '))
    print('Correct!')
    if (input('Would you like to play again? y/n ').lower().strip() # 1, 3
        in ('no', 'n')):                                           # 2
        break

# 1 - My use of methods 'str.lower()' and 'str.strip()' are
#     not necessary, but are included for completeness
# 2 - "...in ('no', 'n')" could as easily be replaced with
#     "...== 'n'" but I chose to include support if the user types
#     'no' as well as just 'n'.
# 3 - I did not assign the result of input() to a variable before
#     comparing it as it is only being used once so an in-place
#     input() would suffice


# My solution to extension 3:

# ...initial 'setup' code...
attempts = 1
while guess != random_num:
    guess = int(input('Enter your guess: '))
    attempts += 1                                        # 1
print('Correct! It took you {} tries'.format(attempts))  # 2

# 1 - 'attempts += 1' is the same as 'attempts = attempts + 1', but
#     using augmented addition, which is faster to type.
# 2 - the 'str.format()' method here replaces the '{}' in the
#     preceding string with the value of 'attempts'. It would be
#     the same to write "'It took you', attempts, 'tries'".


# My solution to extension 4:

# ...initial 'setup' code...
attempts = 1
max_attempts = 20
while guess != random_num and attempts <= max_attempts:  # 1, 2
    guess = int(input('Enter your guess: '))
    attempts += 1
# ...rest of code...

# 1 - This means that the while loops will only continue if the
#     guess is false and the number of attempts hasn't reached
#     the limit.
# 2 - I didn't write the code as 'if attempts > max_attempts: break'
#     instead as this would take up more space and is slower to type.


# My solution to extension 5:

import random
lower = int(input('Enter the lowest number bound: '))   # 1
higher = int(input('Enter the highest number bound: ')) # 1
random_num = random.randint(lower, higher)
# ...rest of code...

# 1 - Personally, I'd prefer to use input validation, but I've
#     excluded it for simplicity


# My solution to extension 6:

# ...initial 'setup' code...

def int_input(prompt):                # 1
    while True:                       # 2
        try:                          # 3
            ans = int(input(prompt))
        except ValueError:            # 4
            print('Bad input!')
        else:
            return ans

guess = int_input('Enter your guess: ')
# ...rest of code... (replace 2nd input later on as well)

# 1 - I decided to create a 'int_input()' function as I will
#     need to perform type validation twice during the code
#     and 2 lots of try/except/else is cumbersome.
# 2 - The 'while True' means it will continue to ask for input
#     until the 'return ans' statement is executed when no
#     error is encountered.
# 3 - The 'try' block means it will attempt to run the code
#     underneath it, but if an exception is raised, then it will
#     be handled below...
# 4 - I only except a 'ValueError' as this is what will be thrown
#     by the 'int(input())' code if a bad input is entered. It is
#     not Pythonic to use a bare 'except' without an exception
#     named as I may catch an exception that I didn't want to.


# My solution taking all the extensions into mind:

import random


def int_input(prompt):
    while True:
        try:
            ans = int(input(prompt))
        except ValueError:
            print('Bad input!')
        else:
            return ans


max_attempts = 20
while True:
    lower = int_input('Enter the lowest number bound: ')
    higher = int_input('Enter the highest number bound: ')
    random_num = random.randint(lower, higher)

    guess = int_input('Enter your guess: ')

    attempts = 1
    while guess != random_num and attempts <= max_attempts:
        if guess < random_num:
            print('Guess higher!')
        else:
            print('Guess lower!')

        guess = int(input('Enter your guess: '))
        attempts += 1

    print('Correct! It took you {} tries'.format(attempts))
    if (input('Would you like to play again? y/n ').lower().strip()
        in ('no', 'n')):
        break
