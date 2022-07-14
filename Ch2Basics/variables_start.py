
myint=5
myfloat=13.2
mystr="this is a string"
mybool=True
mylist=[0,1,"two",3.2,False]
mytuple=(0,1,2)
mydict={'one':1, "two":2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

#re-declaring variables
# myint="abc"
# print(myint)

# to access a member of a sequence
# print(mylist[2])
# print(mytuple[1])

# use slices to get parts of a sequence
# print(mylist[1:5])
# print(mylist[1:5:2])

#using slices to reverse a sequence
# print(mylist[::-1])

#dictionaries are accessed via keys
# print(mydict["one"])

#ERROR: variables of differenct types cannot be combined
# print("string type"+ str(123))

#global vs local variables in functions
def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)

del mystr
print(mystr)