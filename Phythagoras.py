import time

side = input("Which of the sides do you not know the size of (greater, lower, chord) ? ")


if side == 'chord':
    lower_side = float(input("Enter smaller side (cm) = "))
    greater_side = float(input("Enter greater side (cm) = "))
    chord = ((lower_side ** 2) + (greater_side ** 2)) ** 0.5
    print(f"chord (cm) = {chord}")

elif side == 'lower':
    greater_side = float(input("Enter greater side (cm) = "))
    chord = float(input("Enter chord (cm) = "))
    lower_side = ((chord ** 2) - (greater_side ** 2)) ** 0.5
    print(f"lower side (cm) = {lower_side}")

elif side == 'greater':
    lower_side = float(input("Enter smaller side (cm) = "))
    chord = float(input("Enter chord (cm) = "))
    greater_side = ((chord ** 2)-(lower_side ** 2)) ** 0.5
    print(f"greater side (cm) = {greater_side}")

else:
    while True:
        print("write [greater, lower or chord] kesafat !")
        time.sleep(0.3)
