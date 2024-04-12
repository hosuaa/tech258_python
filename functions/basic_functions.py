# Intro to functions

# DRY - Don't repeat yourself

# Function with no argument
def print_something(name):
    print("Hello my name is", name)


print_something("Josh")


# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(2, 2))
# print(addition(20, 5))

# Default arguments

def addition(int1=2, int2=2):
    return int1 + int2


print(addition())
print(addition(20, 5))
print(addition(int2=5))


# multiple arguments

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)


multi_args(1, 2, 3, 4)
multi_args(1, 2)


# type hints
def division(num: int, denom: int) -> float:
    return num / denom


print(division(5, 3))
