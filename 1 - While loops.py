"""Overview of While Loops"""

from functions import demo, placeholders, getinput, Status, Demo

condition = placeholders('false')
another_condition = placeholders('true')
do_stuff = placeholders('function')
do_more_stuff = placeholders('function')



# A while loop, in summary, repeats a section of code
# continuously.

# The repetition goes on until the condition
# specified at the start becomes false; until an
# unhandled exception is raised; or, the while loop
# is broken out from explicitly



# Syntax for while loops:

while condition:       # while condition is True
    do_stuff()

# All of the code in the while loops is indented



# Other information:

# A while loop can be broken out of explicitly
# by adding a 'break' statement
while condition:
    do_stuff()
    if another_condition:
        break
    do_more_stuff()

# You can skip code and start the next repetition of a loop
# by using a 'continue' statement
while condition:
    do_stuff()
    if another_condition:
        continue
    do_more_stuff()  # won't do this code if another_condition os
                     # True as there is a 'continue' statement



demo('Simple Password Checker')
# response = Demo('response')
response = Status('reponse.demo', len, '<', 10)


response.demo = getinput('Enter password: password1', 'password1')
while len(response.demo) < 10:
    response('user input is too short')

    print('Your password must be at least 10 characters long')
    response.demo = getinput('Enter password: StrongPassword',
                            'StrongPassword')

response('user input is long enough')
