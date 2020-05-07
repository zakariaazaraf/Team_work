#----------------------------------------------
#---------     Strings methds III     ---------
#----------------------------------------------

# Index("subString", Start, End) return the index of the charter passed, if the charter doesn't exists it will give an ERROR

a = "i love the c programming language"
print(a.index("c"))  # => return 11
#print(a.index("c", 15, -1))  ==> ERROR cause the charter doesn't exist

# find("subString", Start, End) => same as index() except on the case which the value doesn't exist it return -1
print(a.find("o", 0, -1))  # => 3
print(a.find("c", 15, -1))  # => -1 means that the value doesn't appear

# rjust(number, ["charter"])  |  ljust(number, ["charter"]) [] => optionel
myName = "zakaria"
print(myName.rjust(12))  # ==> "     zakaria"
print(myName.rjust(12, "@"))  # ==> "@@@@@zakaria"

print(myName.ljust(13))  # ==> "zakaria      "
print(myName.ljust(13, "@"))  # ==> "zakaria@@@@@@"
# splitlines() => devide the string line
splitlinesVariable = """first word
second word
third word
"""
print(splitlinesVariable.splitlines(
))  # => return a list of strings ["first word", "second word", "third word"]

# expantabs(tabsize) ==> expan the number of tabs
b = "i\tlove\tpython\tand\tc programming languages"
print(b.expandtabs(2))  # => expand the tab to 2
print(b.expandtabs(5))  # => expand the tab to 5

#------------------------------------------------------------------------------

# function return booleen value
# Str.istitle() ==> is the first charter of each word is capital
# Str.islower()
# Str.isupper()
# Str.isspace()
# Str.isidentifier() => is this string can be a valide variable
# Str.isalpha()
# Str.isalnum() => is the string contain alphabtic and number
