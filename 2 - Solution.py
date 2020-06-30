"""Notes on while loop exercise."""

# Notes:

# This exercise combines the use of while loops, lists
# and lists to expand on previous usage.

# You may need to use multiline strings in this
# exercise to print a menu with options. There are
# a few ways to do this:

print("""Type a number to perform the operation:
1 - Display list
2 - Remove an item
3 - Add an item""")  # Using a multiline string is easy and
# clear, however, make sure that new lines are not indented
# otherwise they will appear indented too.

print('Type a number to perform the operation\n1 - Display list\n2...')
# A newline escape character '\n' can be used in a string to denote
# a new line break. This method is not recommended for long strings
# as the line will quickly become long and unreadable

print('Type a number to perform the operation')
print('1 - Display list')     # Using individual 'print' statements
print('2 - Remove an item')   # is also another viable option. The
print('3 - Add an item')      # readability is the same as the
# multiline string approach, but requires more typing for each
# 'print' - which is each line



# Approach:

# First, start off by setting up the variables we will need to use:
shopping_list = ['Apples', 'Biscuits', 'Milk', 'Bread']
ans = ''  # Will be changed below...

# I tend to use 'ans' as a variable to hold user input that
# is a string. Note that for numbers I'd use 'num/number/val/value'

# Now, setup the menu system. This will consist of a text being
# displayed, an input received, and choosing what to do next
# depending on the input:
print('Type a number to perform its action:')
print("""1 - Display list contents
2 - Add an item
3 - Remove an item
4 - Exit""")
ans = input()
if ans == '1':
    pass
elif ans == '2':
    pass
elif ans == '3':
    pass
elif ans == '4':
    pass
else:
    print('Invalid choice. Please pick again.')

# The 'pass' statement just means no code will be executed. I'll
# Fill them in below...

# Fill in the first 'pass' statement with the code
# for option 1 which displays the list:
if ans == '1':
    print('Your current cart contents are:\n', shopping_list)

# Fill in the 'pass' statement under option 2 which adds an
# item to the list:
elif ans == '2':
    shopping_list.append(input('Choose item: '))

# I put the input() straight into the list.append() method as
# I'll only need the value once so it would be redundant to
# store it in a variable for a single use.

# Fill in the 'pass' statement under option 3 which removes
# an item from the list.
elif ans == '3':
    shopping_list.remove(input('Choose item: '))

# Before I add the code for option 4, we need to wrap the code in
# a while loop to make sure that after we finish doing an action,
# the menu is displayed again:
while True:
    print('Type a number to perform its action:')
    print("""1 - Display list contents
2 - Add an item
3 - Remove an item
4 - Exit""")
    ans = input()
    if ans == '1':
        print('Your current cart contents are:\n', shopping_list)
    elif ans == '2':
        shopping_list.append(input('Choose item: '))
    elif ans == '3':
        shopping_list.remove(input('Choose item: '))
    elif ans == '4':
        pass
    else:
        print('Invalid choice. Please pick again.')

# Now we can add the code for option 4:
elif ans == '4':
    print('Exiting...')
    break

# The 'break' statement will exit the 'while' loop. As there is no
# code after the while loop, the program will end



# Solutions:

# My solution to the original task:

shopping_list = ['Apples', 'Biscuits', 'Milk', 'Bread']
while True:
    print('\n\nType a number to perform its action:\n')      # 1
    print("""1 - Display list contents
2 - Add an item
3 - Remove an item
4 - Exit""")
    ans = input()
    if ans == '1':
        print('Your current cart contents are:\n', shopping_list)
    elif ans == '2':
        shopping_list.append(input('Choose item: ').title())  # 2
    elif ans == '3':
        shopping_list.remove(input('Choose item: ').title())  # 2
    elif ans == '4':
        print('Exiting...')
        break
    else:
        print('Invalid choice. Please pick again.')

# 1 - I added some newline '\n' escapes here. This is purely for
#     aesthetic reasons and is not necessary. It just separates
#     a new menu from whatever is above it
# 2 - I used str.title() here to make sure that all items being
#     added are capitalised and when removing items, I capitalised
#     the input to make sure that it finds the item even if a
#     non-matching-case input is entered


# My solution to extension 1:

# ...initial code...
while True:
    print('\n\nType a number to perform its action:\n')
    print("""1 - Display list contents
2 - Add an item
3 - Remove an item
4 - Insert an item
5 - Exit""")                                                       # 1
    ans = input()
# ...some 'if' statements here...
    elif ans == '4':
        while True:
            try:                                                   # 2
                ans = int(input('Enter index (0 or more)'))
            except ValueError:
                print('Invalid index')
            else:
                if 0 <= ans:                                       # 3
                    break
        shopping_list.insert(ans, input('Choose item: ').title())  # 4
    elif ans == '5':
        print('Exiting...')
        break
# ...rest of code...

# 1 - I added a line here for the new option and pushed 'Exit' down
#     to number 5
# 2 - I chose to use a try/except block for input validation for
#     completeness, but this could be omitted for simplicity
#     and replaced with just 'int(input())'
# 3 - Even if the casting to integer succeeds, I still needed to
#     make sure it was at least 0. Only then did I stop the loop
# 4 - I used input().title() directly in the list.insert() method
#     as I'd only need the value given once and I capitalised it
#     so that it is consistent with the rest of the list


# My solution to extension 2:

# ...previous 'if' statements
elif ans == '3':
    ans = input('Choose item: ').title()    # 1
    if ans in shopping_list:                # 2
        shopping_list.remove(ans)
    else:
        print('That item does not exist')
# ...rest of 'if' statements...

# 1 - I needed to store the input in a variable this time as it
#     would need to be used twice in the code. I chose to reuse
#     the 'ans' variable here.
# 2 - The 'in' operator tests whether an item is inside a container
#     (in this case, the list) and if it is inside, I removed it,
#     otherwise, I displayed a small error message


# My solution to extension 3:

if ans == '1':
        print('Your current cart contents are:')
        print('\n'.join(shopping_list))              # 1, 2

# 1 - This str.join() method places a string (here, a newline '\n')
#     in between each item in the iterable (list). This is a
#     much quicker version of the following below....
# 2   I replaced 'str(i) for i in shopping_list' here with simply
#     just 'shopping_list' as I know that all items are going
#     to be a string anyway.

if ans == '1':        # (from 1)
        print('Your current cart contents are:')
        for item in shopping_list:                   # 3
            print(item)

# 3 - The 'for' loop iterates over each item in the list. Each item
#     is assigned to 'item' (given in the for loop).


# My solution to extension 4:

if ans == '1':
        print('Your current cart contents are:')
        print('\n'.join('{}: {}'.format(n, i)                      # 1
                        for n, i in enumerate(shopping_list)))     # 2

# 1 - This is a pretty quick way of looping over a list
#     and displaying it, using the item and its index
# 2 - 'enumerate()' will return a pair of values (which I called
#     'n' and 'i') which are the index and item respectively
#     The line could be replaced with the following, without using
#     enumerate(), but just a 'for' loop:

count = 0        # (from 1, 2)
for item in shopping_list:
    print(str(count) + ': ' + str(item))  # (2nd 'str()' not needed)
    count += 1   # (count = count + 1)


# My solution considering all extensions:

shopping_list = ['Apples', 'Biscuits', 'Milk', 'Bread']
while True:
    print('\n\nType a number to perform its action:\n')
    print("""1 - Display list contents
2 - Add an item
3 - Remove an item
4 - Insert an item
5 - Exit""")
    ans = input()
                                                                # 1
    if ans == '1':
        print('Your current cart contents are:')
        print('\n'.join('{}: {}'.format(n, i)
                        for n, i in enumerate(shopping_list)))

    elif ans == '2':
        shopping_list.append(input('Choose item: ').title())

    elif ans == '3':
        ans = input('Choose item: ').title()
        if ans in shopping_list:
            shopping_list.remove(ans)
        else:
            print('That item does not exist')

    elif ans == '4':
        while True:
            try:
                ans = int(input('Enter index (0 or more)'))
            except ValueError:
                print('Invalid index')
            else:
                if 0 <= ans:
                    break
        shopping_list.insert(ans, input('Choose item: ').title())

    elif ans == '5':
        print('Exiting...')
        break

# 1 - I added some whitespace between each if statement to ease
#     readability for users (and myself).
