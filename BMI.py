import webbrowser


url = "https://www.who.int/tools/growth-reference-data-for-5to19-years"

print("This is a BMI test\n\n")
age = int(input("Enter your age: "))
height = float(input("Enter your height (cm): "))
weight = float(input("Enter your wight (kg): "))
height = height / 100
BMI = weight/(height**2)
BMI = (BMI * 100) // 1
BMI = BMI / 100
print(f"\nyour BMI is: {BMI}")

if age >= 19:   
    if BMI < 18.5:
        print("status: underweight.")
    elif BMI >= 18.5 and BMI <= 24.5:
        print("status: healthy")
    elif BMI >= 25 and BMI <= 29.9:
        print("status: overweight")
    else:
        print("status: obese")
    healthy_weight_1 = 18.5 * (height ** 2)
    healthy_weight_2 =25 * (height ** 2)
    amount_of_excess_weight = weight - healthy_weight_2
    print(f"Amount of excess weight: {round(amount_of_excess_weight, 1)} kg")
    print(f"Healthy weight range: {round(healthy_weight_1, 1)} to {round(healthy_weight_2, 1)} kg")
else:
    print("\nNOTE:")
    print("To interpret your BMI, check the percentile table on the official website.")
    while True:
        ans = input("Do you want to open the link?\n(yes/no): ").strip().lower()
        if ans == 'yes':
            print("Opening the link")
            webbrowser.open(url)
            break
        elif ans == 'no':
            print("Okay! good luck.")
            break
        else:
            print("Just write yes or no.")
