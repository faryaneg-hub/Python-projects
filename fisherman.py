import random

pound = float(input("Enter the weight of fish in pounds: "))


kilogram = pound * 0.45359237


money = kilogram * 2

print("Weight in kilograms:", kilogram)
print("Money received:", money, "dollars")


if money > 100:
    prize = random.choice(["Hat", "Hook", "Bucket"])
    print("Your prize is:", prize)
