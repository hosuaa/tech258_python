# Bools and None

# Booleans can be True or False (capitalized)

a = True
b = False

print(a == b)
print(a != b)

# False is always 0
print(a >= b)

# Boolean methods
hi = "Hello World!"
print(hi.isalpha())  # False since there's a space in it
print(hi.islower())  # False since H and W
print(hi.isupper())
print(hi.endswith("!"))
print(hi.startswith("H"))

# Always true unless the string is empty
print(bool(hi))  # True
print(bool(""))  # False

# Always true unless its 0
print(bool(0))  # False
print(bool(40))  # True

# None
# None is an object, its essentially a placeholder
# None when cast to bool is False
print(bool(None))
# But None != False
x = None
print(x == False)  # False - prefer x is False
print(x == None)  # True - prefer x is None

print(type(x))  # NoneType

# A None variable is best used over an empty string as a placeholder
# -less likely to cause problems + takes up less memory

