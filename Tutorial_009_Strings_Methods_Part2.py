#----------------------------------------------
#---------     Strings methds II     ----------
#----------------------------------------------

# Str.split() => devide the string on word based on the space(defultSepartor) between words
# # Str.split("Separtor",Number) => Separtor == , or - ...    Number == 2, 3, 4...
# Str.rsplit(",",Number) => like the preveous one but start from the right side

a = "I love C And Python and Sql"
print(a.split())  # it return a list of items
print(type(a.split()))

b = "I love C And Python and Sql"
print(b.rsplit(
    " ", 4))  # it will return a list of 3 items and the rest as another Item

c = "I-love-C-And-Python-and-Sql"
print(c.split("-", 3))  # it return a list of items

listOfItem = c.split("-")
print("the value of this item is : " + listOfItem[0] + " " + listOfItem[1] +
      " " + listOfItem[2])

# Str.center(Number)  ==> take a NumberParameter and retuen the string arounded by the charterParameter or the defult (Space)
# Str.center(Number,"charterPara")  ==> take a NumberParameter and retuen the string arounded by the charterParameter

name = "zakaria"
print(name.center(11))  #   ==> "  zakaria  "
print(name.center(11, "&"))  #   ==> "&&zakaria&&"

# Str.count() ==> return the number of word specific inside the string
# Str.count("charter", Start, End) ==>

countVariable = "I c love and python but forver c"
print(countVariable.count("c"))
print(countVariable.count("c", 2, 15))  # it return one which is the first C

# Str.swapcade() ==> it change charter from capital to small and vice versa

aa = "i loVe Python AND c"
bb = "I LOVE python and C"
print(aa.swapcase())  # => I LOvE pYTHON and C
print(bb.swapcase())  # => i love PYTHON AND c

# startwith()  ("Charter", Start, End) ==> return booleen value if the charter exist
# endtwith()  ("Charter", Start, End) ==> return booleen value if the charter exist

sWith = "i love c language"
print(sWith.startswith("i"))  # true
print(sWith.startswith("l", 4, 10))  # false
print(sWith.startswith("c", -10, -1))  # true

eWith = "i love c language"
print(eWith.endswith("age"))
print(eWith.endswith("c", 1, -9))
