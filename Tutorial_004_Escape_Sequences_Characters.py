# --------------------------------------------------------
#------------   escape sequences characters  -------------
#  \b back space == remove the charter before \b
#  \ newLine == new line and back slash
#  \\  == Escape Back Slash
#  \'  == Escape Single Quote
#  \"  == Escape Double Quotes
#  \n  == line feed it work like C Language
#  \r  == carriage return it repalce charters insteade of anothers
#  \t  == Horizontal tab it work like C Language
# --------------------------------------------------------

# back space
print("testing\b this app")  # it well remove g charter

# new line
print("Hello \
i love \
python")

# Escape back slash
print("Zakaria \\Hicham \\Radouane")

# Escape single quote
print('i like \'BLACK\' color')

# Escape double quotes
print("i like \"BLACK\" color")

# line feed
print("Our company genius are\nZakaria\nHicham\nRadouane")

# Carraiage Return
print("ABCDEF\r123")  # => it well print 123DEF
print("123456\rABC")  # => it well print ABC456
