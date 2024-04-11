# BMI Calculator

height = float(input("Enter your height (m):"))
weight = float(input("Enter your weight (kg):"))

bmi = weight / (height * height)

print("Your BMI is: ", round(bmi, 2))
