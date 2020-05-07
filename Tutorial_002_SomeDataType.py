#----------------------------------
# some data type in python
# type() return the type of a date
# All data in python is object
#----------------------------------
print(type(10))  # Int == Intger number

print(type(10.25))  # float == floating point number

print(type("i love python"))  # str == string type

print(type([
    1, 2, 3, 4, 5
]))  # list == list, not an array like other programming language pay attention

print(type((1, 2, 3, 4, 5)))  # tuple == tuple it's a new data for me

print(type({
    "one": 1,
    "two": 2,
    "tree": 3
}))  # dict == Dictionary  and not an object cause alrady data are objects
