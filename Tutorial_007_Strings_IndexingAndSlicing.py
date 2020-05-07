#-------------------------------------------
#----    Indexing & Slicing of Str    ------
#-------------------------------------------

# [1] all data in python are objects
# [2] Objects contain elements
# [3] Use square Brackets to Access Elements
# [4] Enable Accessing to strings, tuples or list
#------------------------------------------------------------

# Indexing | Access Single Item
myString = "I love phthon"
print(myString[2])  # Index 2 => It will print  'l'
print(myString[7])  # Index 7 => It will print  'p'

print(
    myString[-1])  # Index -1 => It will print  'n' cause it begin from the end
print(myString[-10])  # Index -10 => It will print  'o'

# Slicing | Access multiple Sequance item
# myString[Start:End] End not included
# myString[Start:End:Step]

print(myString[2:7])  # it will print 'love'
print(myString[0:-2])  # it will print 'I love phth'
print(myString[7:-2])  # it will print 'puth'

# Example with Step
print(myString[2:7:1])  # defult step is 1
print(myString[2:7:2])  # it will print "lv"
