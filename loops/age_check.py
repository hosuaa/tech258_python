# Age check

# SET VARIABLE user_prompt TO TRUE
user_prompt = True
# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")
    # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
    if age.isdigit():
        # SET user_prompt TO FALSE
        # check user age too
        if 117 > int(age) > 0:  # equivalent to int(age)>0 and int(age)<117
            user_prompt = False
        else:
            print("Invalid age: Only numbers between 0 and 117 are allowed")
    # ADD ELSE STATEMENT HERE
    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT
        print("Invalid age: Only numbers are allowed")

print(f"Your age is {age}")
