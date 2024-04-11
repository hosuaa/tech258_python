# Sets and Frozen Sets

fruits = {"apple", "banana", "cherry"}
# Unordered!!
print(fruits)  # Every time you run this the order will be different

# Sets are unordered and unindexed - cant do fruits[1] (not subscriptable)
# You can access set elements by e.g. for item in set: (item is each item)

fruits.add("orange")
print(fruits)

fruits.remove("apple")
print(fruits)

# Cannot add duplicates
fruits.add("banana")
print(fruits)

# Convert a list to a set to remove duplicates
example = ["one", "two", "three", "one"]
no_dupes = set(example)
print(no_dupes)

# Sets are smaller and so more efficient to use
# Good way to randomize data

# A set of integers is not randomized (unordered)
int_set = {1, 2, 3, 4}
print(int_set)  # Prints 1, 2, 3, 4 always

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
print(set_a | set_b)  # Union
print(set_a - set_b)  # Difference (1,2 cos whats in set_a and not set_b)

# Frozen set -> immutable set
frozen_set = frozenset(["hello", "world"])
print(frozen_set)
# Why? Multi threading or...
# Sets within sets
# You can only add hashable items to sets - the immutable thing, similar to tuples
normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)
