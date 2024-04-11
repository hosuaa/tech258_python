# Strings

single_quotes = 'single'
double_quotes = "double"

print(single_quotes)
print(double_quotes)

# generally use double quotes because ' has more use in language

# bad_string = 'It's not right'
good_string = "It's not right"
print(good_string)

# if you really need to use ''
escape = 'I said \'Wow\''
print(escape)

# string slicing
hw = "Hello World!"
# how many characters in hw?
hw_len = len(hw)
print(hw_len)
# get the first letter in hw
hw_first = hw[0]
print(hw_first)
# get the last letter
hw_last = hw[hw_len - 1]
print(hw_last)
# use negative indexing to get the 2nd last letter
hw_penultimate = hw[-2]
print(hw_penultimate)
# get the first 3 letters
hw_three = hw[0:3]
print(hw_three)

# string methods
white_space = "lots of white space at the end                                 "
stripped = white_space.strip()
print(stripped)

example_string = "Here's some text with lots of text"
# count a substring within a string: can also check characters and spaces etc
print(example_string.count("text"))  # 2

print(example_string.lower())

print(example_string.upper())

print(example_string.capitalize())  # beginning of string

print(example_string.replace("with", ","))

# concatenation
a = "here "
b = "more "
c = "much more"
print(a + b + c)

x = 2
y = 5.4
z = " theres now a number 25.4"
w = "30"
print(str(x) + str(y) + z)
print(x + y + int(w))

# F-string
# name = "lassie"
# years = 7
# height_cm = 60.2

# put f before the string then whenever you want to put a variable in put it in squiggly brackets
# print(f"{name} is {years} years old and {height_cm} tall")

name = "Snoopy"
years = 52
# in f strings we can also call string methods on the variables passed
print(f"{name.upper()} is {years * 7} years old in dog years")

# using f-strings to format numbers
pi = 3.14159265359
print(f"pi to 3 dp. is {round(pi,3)}")  # can also do {pi:.3f} 3f means 3 after the dp.
print(f"pi to 5 dp. is {round(pi,5)}")  # without the 3f (just 3) its 3 total digits (so 3.14 is displayed not 3.142)
