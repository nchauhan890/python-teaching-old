"""Overview of lists."""

from functions import demo, placeholders, getinput, Status, Demo

index = placeholders('index')
item = placeholders('item')
lst = placeholders('filled_list')
slice2 = placeholders('slice2')
slice3 = placeholders('slice3')



# A list is, well, a list of things. They are similar to
# arrays in other programming languages.

# They can contain any data type and hold any number of
# items (to an extent).



# Syntax for lists:

empty_list = []
filled_list = [1, 'Hello', 3.75]

# Lists use square brackets [] with comma-separated values inside



# List methods:

# add an item to the end of a list
lst.append(item)

# remove the first occurence of an item
lst.remove(item)

# remove an item by index
lst.pop(index)

# add an item at the index given
lst.insert(index, item)

# join 2 lists together
lst.extend(lst)

# count the number of times an item appears in the list
lst.count(item)

# get the number of items in the list
len(lst)

# get an item by its index in the list - the first item
# has an index of 0. The last item in the list can be
# retreived using -1 as the index. The index of the last
# item is 1 less than the list's length
lst[index]
lst[1]        # 2nd item in list
lst[-2]       # 2nd from last item

# get a portion of items out of a list using a slice:
# the 1st is the starting index and the 2nd is the ending
# index which is not included. So a slice of 1:4 will return
# items at index 1, 2, 3 (but not 4).
lst[slice2]
lst[0:3]
lst[:3]     # omitting 1st value means it starts at the start
lst[2:]     # omitting 2nd value means it finishes at the end

# A third parameter can be given which denotes the 'step' rate.
# A step of 2 means it will return the items but skip every other item
lst[slice3]
lst[0:4:2]    # the indexes 0, 2 are returned
lst[1::3]     # the indexes 1, 4, 7, etc... are returned until the end
              # of the list as the end parameter is omitted



demo('List of Numbers')
numbers = Demo('numbers')
results = Demo('result')


numbers.demo = [1, 2, 3, 4, 5, 6, 7, 8]
numbers('create a list of numbers from 1 to 8')

numbers.demo.append(9)
numbers('add 9 to the end of the list')

numbers.demo.insert(0, 0)
#              index^  ^item
numbers('add number 0 to the start')

results.demo = numbers.demo[3]
results('retreive index 3 from the list')

results.demo = numbers.demo[4:7]
results('get items 4-7 (excluding 7) from the list')

results.demo = numbers.demo[:8:3]
results('get every 3rd item up to, but not including, 8')
