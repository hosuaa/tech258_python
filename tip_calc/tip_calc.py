# Tip Calculator

bill = float(input("Enter total bill (£):"))

tip = bill * 0.15

bill_with_tip = bill + tip

people = int(input("How many people are splitting the bill?"))

bill_with_tip_split = bill_with_tip / people

print("Each pays ", round(bill_with_tip_split, 2))
