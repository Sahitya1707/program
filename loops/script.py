# in python there are two way for loopin though okay? that is either by for loop or while loop
numbers = [2,3,4,5]
for n in numbers:
    print(n)


#  for loops can also iterate over a sequnc eof number range and xrange
for x in range(5):
    print(x) # print from 0 - 4

# let's use while loop okay? 
count = 0
while count < 5:
    print(count)
    count +=1 # this will add 1 to count every time okay? 
    #  Let's use break and continue state as well

value = 0
while True:
    print(value)
    value += 1
    if value >=5:
        break # we will add a break if value has reach 5 or greater than that

#prints out only odd number 
for x in range(10):
    if(x%2 == 1):
        print(x) # odd number



