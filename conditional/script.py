x = 2
print(x == 2) #true
print(x == 3) # false x is not equal to 3
print(x < 3) # true x is less than 3

# what about boolean operator though?

name="John"
age=23
if name == "John" and age==23:   # and operator mean both need to be true to get the outcome true
    print('You name is %s and your age is %d' % (name, age))

if name == "John" or age==2:  # one one thing need to be true in this case
    print('One thing true either name or age')

# In operator
food = "rice"
if food in ["rice", "bagel"]:
    print('Your food is either rice or bagel.')

# if else statemenet in python
statement = False
another_statement = False
if statement is True: # here3 we have used is operator as well okay? 
    print('statement is true')
    pass
elif another_statement is True:
    print('another stemenent is true')
    pass
else:
    print('Nothing is true')
    pass


# not operator - reverse
print(not False)