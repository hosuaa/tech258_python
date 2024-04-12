# Loops

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# 1. Print each list_data twice
for num in list_data:
    print(num * 2)
    #print(num)

# 2. Print items in embedded list
for l in embedded_lists:
    print(l)

# 3. Print individual items
for l in embedded_lists:
    print(l)
    for num in l:
        print(num)

# 4. Loop through dict_data
for key, values in dict_data.items():
    print(key)

# 5. Print values in dict_data
for key, value in dict_data.items():
    print(value.values())

# 6. Print the values on seperate lines
for key, value in dict_data.items():
    for v in value.values():
        print(v)

# 6. Only print the money
# for key,value in dict_data.items():
#     for v in value.values():
#         print(v)
print(dict_data.values())
for value in dict_data.values():
    print(value["money"])

# 7.
for num in list_data:
    if num < 3:
        print("Less than 3")
    elif num == 3:
        print("I found 3")
    else:
        print("More than 3")
