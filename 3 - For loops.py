"""Overview of for loops"""

from functions import demo, placeholders, getinput, Status, Demo

iterable = placeholders('filled_list')
do_stuff = placeholders('function')
condition = placeholders('false')


# For loops allow an iterable (such as a list) to be
# iterated over. This means that each item in the iterable
# will be returned and used in the loop.

# Each time the loop repeats, a new object from the
# iterator is used. The for loop ends when there are
# no more items in the iterable left to return, or
# if the loop is explicitly broken out of.



# Syntax for for loops:

for item in iterable:
    do_stuff(item)



# Other information:

# A common use of a for loop is to use a sequence of
# numbers, where the number increases by one for each
# repetition. You could do the following to print
# the numbers 0-9:
count = 0
while count < 10:
    print(count)
    count += 1

# However, the cleaner solution is to use a for loop:
for count in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
    print(count)
    # count automatically increases, so we don't need to
    # explicitly increase it

# An even cleaner solution is to use the built-in
# range() function which returns an iterator that yields
# successive numbers. It works much like list slicing,
# where the range starts at the first number and ends
# at, but not including, the end number. A 3rd parameter,
# step, is also available to yield values of a certain
# multiple:
for count in range(10):
    print(count)

# If you omit the first value, 0, it assumes the value is 0
# automatically so range(10) == range(0, 10)

# For loops can be broken out of by using a 'break' statement
# like in while loops:
for i in range(30):
    if i % 12 == 0 and i > 20:  # if 'i' is divisible by 12
        break                   # and more than 20: it will
    print(i)                    # break at the number 24
# (prints the numbers 0 to 23)

# Code can be skipped and the next repetition started by using
# a 'continue' statement:
for item in iterable:
    if condition:
        continue
    do_stuff(item)

# The built-in enumerate() function can be used to return the
# item yielded by the iterator along with the number of the
# current iteration. The values should be unpacked by specifying
# 2 parameters in the for loop, the first is always the index
# from enumerate():
for index, item in enumerate(['apple', 'banana', 'orange']):
    print('{}: {}'.format(index, item))
# Prints the following:
# 0: apple
# 1: banana
# 2: orange

# The enumerate() function allows for a cleaner solution as
# opposed to the following: (This method also has downsides
# when there are duplicate item in the list)
fruits = ['apple', 'banana', 'orange']
for item in fruits:
    index = fruits.index(item)
    print('{}: {}'.format(index, item))

# A version that is list-specific (or tuple):
count = 0
for item in fruits:
    print('{}: {}'.format(count, item))
    count += 1

# The equivalent of using a for loop to iterate over a list using
# a while loop is as follows.
# Note that StopIteration is an exception raised when the iterator
# has no more items to yield:
iterable = iter(iterable)
while True:
    try:
        next(iterable)   # do stuff with the value returned from next()
    except StopIteration:
        break           # end when there are no more values



demo('Fibonacci sequence up to 10th number')

a = Demo('a')
b = Demo('b')

a.demo = 1
b.demo = 1
a('create starting values of 1 and 1')

print('Fibonacci number 1: {}'.format(a.demo))

for i in range(2, 11):
    print('Fibonacci number {}: {}'.format(i, b.demo))

    a.demo, b.demo = b.demo, a.demo + b.demo
    a('set a to b')
    b('set b to the value of a + b')
    # use of variable swapping using tuple unpacking:
    # a, b = b, a + b

