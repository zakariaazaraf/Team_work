#----------------------------------------------
#---------     Strings methds I     -----------
#----------------------------------------------

# len() method ==> return the number of charters
# [str].strip() [str].rstrip() [str].lstrip() remove space or a charter passed in paramter from right or left or both of

myValue = "I love python"
print(len(myValue))

myVariable = "   I love python    "
print(myVariable.strip())
print(myVariable.rstrip())
print(myVariable.lstrip())

myVar = "###I love python#####"
print(myVar.strip("#"))  # remove '#' charter from both sides
print(myVar.rstrip("#"))  # remove "#" from right side
print(myVar.lstrip("#"))  # rm "#" from left side

# [str].capitalize() => make the first charter of the string capital
myCapital = "i love 2d graphics and 3d games"
print(myCapital.capitalize())

# [str].title() => it capitalize the first charter of each words
print(myCapital.title())

# [str].zfill() => zero fill, it add zero to left like 001
a, b, c = "1", "11", "111"
print(a.zfill(3))  # ==> 001
print(b.zfill(3))  # ==> 011
print(c.zfill(3))  # ==> 111

# [str].upper() => capitalize all string
first = "zakaria"
print(first.upper())

# [str].lower() => make the string small
second = "AZARAf ZIKO"
print(second.lower())
