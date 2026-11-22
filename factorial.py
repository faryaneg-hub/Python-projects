number = int(input("Number: "))
fac = 1
for i in range(1, number+1):
    fac *= i
print(f"factorial of number {number} = {fac}")
