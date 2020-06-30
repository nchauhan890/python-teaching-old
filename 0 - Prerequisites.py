"""Prerequisites for these sections."""

from functions import placeholders

condition = placeholders('false')
iterable = placeholders('filled_list')
x = placeholders('item')

# I'm assuming that you have a decent idea about
# and can use the following ideas to produce simple,
# but functional programs:



#                  Data Types                      #

# Strings:
'Hello World!'

"""
- Can be wrapped in either ' ' or " "
- Multiline string use
  triple quotes: ''' ''' or \""" \"""
- Use str() to convert something into a string:
"""
str('hello')    == 'hello' # (already a string)
str(10)         == '10'
str(3.5)        == '3.5'
str(True)       == 'True' # (the same for False)


# Int and Float
1, 210 and 12.5, 3.14159

"""
- Integers are whole numbers
- Floats are numbers with a decimal point
- Use int() and float() to convert into an int
  or float respectively, assuming that they
  can be converted:
"""
int('25')   == 25
int(9.72)   == 9  # (the decimal is dropped
                  #  without rounding off)
int('9.72') == ValueError # (it would need to
                          #  be converted to
                          #  a float)

float('25')    == 25.0
float(9.72)    == 9.72  # (already a float)
float('9.72')  == 9.72


# Boolean
True, False
"""
- Represent the number value 1 and 0 respectively
  in most contexts other than when converted
  through str()
- Every value that is not 0 is considered True
- Use bool() to convert to a boolean; everything
  except 0 will return True (most of the time)
"""
bool(1)    == True
bool(0)    == False
bool(0.0)  == False
bool(0.01) == True
bool('0')  == True  # (surprisingly, it returns True as
                    #  the value inside the string is
#  ignored, just the fact that it is a string means it
# isn't 0 or 0.0; therefore it returns True)



#                   Variables                      #

"""
- Variables can hold a value for use later
- Their value can vary - hence their name
- Can be assigned to using =
- Cannot be used unless they've been assigned
  to previously
"""
thing = 'book'           # assignment
print(x*2)  == NameError # 'x' has not been assigned to
                         # previously, so python doesn't know
                         # what it is
y = 5
print(y*5)               # prints '25' as 'y' has been
                         # assigned to the value 5 and is being
                         # multiplied by 5 here



#                   Operators                      #

"""
+               addition
-               subtraction
/               division
*               multiplication

//              floor division (rounds down and gets rid of decimal)
**              exponent (raise a number to a power: 3**2 is 3 squared)

%               modulus (return the remainder after dividing:
                11 % 3 returns 2 as 11 / 3 is 3 remainder 2)

==              equals to
!=              doesn't equal to
>               greater than
<               less than
>=              greater than or equal to
<=              less than or equal to

and, or, not    logical
in, not in      membership
is, is not      identity
"""



#                Print Function                    #

"""
- Displays the information inside the function
  as a string on the output
- By default, a new line is inserted before each new print
"""

print(1)                       == '1'  # displays 1

print('Hello there ', end='')  == 'hello there'  # prints as usual
print('Bob')                   == 'Bob'  # however Bob appears on
                                         # the same line as the
# previous print as the 'end' keyword argument was specified as
# blank instead of its default newline '\n'



#                  Flow control                      #

"""
- Basic use of 'if' statements along with 'elif' and 'else'
- Idea that 'elif' is used as 'else, if'
- Basic use of 'while' loops
- (Awareness of 'for' loops)
"""
if condition:     # if condition is True
    pass
elif condition:   # otherwise, if this condition is True
    pass          # (optional, but may only be used before 'else'
                  #  and after 'if')

else:             # otherwise do this if the rest fail (optional)
    pass


while condition:  # while condition is True
    pass


for item in iterable:    # iterate over something
    pass                 # (use the 'item' parameter named above)
