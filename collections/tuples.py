# Tuples

# Tuples are immutable (cannot change after declaration)
# Reasons for tuples:
# 1. ensure data remains constant
# 2. faster execution (tuples are smaller - take up less memory - than mutable data structures such as lists)

# from https://stackoverflow.com/questions/2174124/why-do-we-need-tuples-in-python-or-any-immutable-data-type

# As you point out, tuples are immutable. The reasons for having immutable types apply to tuples:
#
# copy efficiency: rather than copying an immutable object, you can alias it (bind a variable to a reference)
# comparison efficiency: when you're using copy-by-reference, you can compare two variables by comparing location, rather than content
# interning: you need to store at most one copy of any immutable value
# there's no need to synchronize access to immutable objects in concurrent code
# const correctness: some values shouldn't be allowed to change. This (to me) is the main reason for immutable types.
# Note that a particular Python implementation may not make use of all of the above features.
#
# Dictionary keys must be immutable, otherwise changing the properties of a key-object can invalidate invariants of the underlying data structure. Tuples can thus potentially be used as keys. This is a consequence of const correctness.
#
# See also "Introducing tuples", from Dive Into Python.

# and

# Before we continue, make sure that the behavior demonstrated below is what you expect from Python.
#
# >>> a1 = [1]
# >>> a2 = a1
# >>> print a2[0]
# 1
# >>> a1[0] = 2
# >>> print a2[0]
# 2
# In this case, the contents of a2 was changed, even though only a1 had a new value assigned. Contrast to the following:
#
# >>> a1 = (1,)
# >>> a2 = a1
# >>> print a2[0]
# 1
# >>> a1 = (2,)
# >>> print a2[0]
# 1
# In this latter case, we replaced the entire list, rather than updating its contents. With immutable types such as tuples, this is the only behavior allowed.
#
# Why does this matter? Let's say you have a dict:
#
# >>> t1 = (1,2)
# >>> d1 = { t1 : 'three' }
# >>> print d1
# {(1,2): 'three'}
# >>> t1[0] = 0  ## results in a TypeError, as tuples cannot be modified
# >>> t1 = (2,3) ## creates a new tuple, does not modify the old one
# >>> print d1   ## as seen here, the dict is still intact
# {(1,2): 'three'}
# Using a tuple, the dictionary is safe from having its keys changed "out from under it" to items which hash to a different value. This is critical to allow efficient implementation.

essentials = ("bread", "eggs", "milk")
print(type(essentials))

