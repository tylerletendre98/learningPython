#define a basic function
from cgitb import reset


def func1():
    print('I am a function')

#function that takes arguements
def func2(arg1,arg2):
    addnumbers=(arg1 + arg2)
    return addnumbers

#function that returns a value
def cube(x):
    return x * x * x

#function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result  

#function with variable number of arguements
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# func1()
# print(func1())
# print(func1)

# print(func2(10,20))
# print(cube(3))

# print(power(6))
# print(power(2,3))
# print(power(x=3, num=2))

print(multi_add(3,2,5,6,7,5))