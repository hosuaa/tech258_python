# Simple calculator
import calculator_operators as calc
# OR: from calculator_operators import add,...  and then remove calc from the .add on 7.

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
result = calc.add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")

