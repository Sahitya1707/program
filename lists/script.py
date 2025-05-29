# list is similar to the array 

myList = []
# append 1 inside the list
myList.append(1)
myList.append(2)

print(myList) # [1,2]

print(myList[0])  # 1
print(myList[1])  # 2
# Looping through array
for x in myList:
    print(x)


# LITTLE EXERCISE OF LIST
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

# write your code here
second_name = None


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % names[1])


#printing the length
print(len(names))

# you can also use list() constructor to make a python list