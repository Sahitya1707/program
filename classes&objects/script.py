# objects are an encapsulation of variable and functions int a single entity.
class MyClass:
    variable = "blah"

    def function(self):
        print('This is a message inside the class')


myobjectx = MyClass()
myobjecty = MyClass()
myobjecty.variable = "no no"

print(myobjectx.variable)
print(myobjecty.variable)


# init functions are special kind of function that is called when the class is being initiated
class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number
    
var = NumberHolder(7)
print(var.returnNumber())