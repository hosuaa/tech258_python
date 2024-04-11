# User details

# 1.
name = input("What is your name? ")
age = int(input("What is your age? "))
dob = input("What is your DOB? ")
# print("Hi", name, "you are", age, "years old and born on", dob)
# 2.
user_details_list = [name,age,dob]
# 3.
print(user_details_list)
# 4.
print(type(age))
# 5.
height = float(input("What is your height? "))
# 6.
user_details_list.append(height)
print(user_details_list)
