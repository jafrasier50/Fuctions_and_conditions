print("||Four Function Calculator||")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

import calcmod

calcmod.addition
calcmod.subtraction
calcmod.multiplication
calcmod.division

choice = None

while True:
    choice = int(input("|Enter Choice|--> 1 | 2 | 3 | 4 : "))
    if choice not in [1, 2, 3, 4]:
        print("Invalid Input. Try Again?")
    else:
        break
        continue

first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

if choice == 1:
    print(first_number, "+", second_number, "=", first_number + second_number)
elif choice == 2:
    print(first_number, "-", second_number, "=", first_number - second_number)
elif choice == 3:
    print(first_number, "x", second_number, "=", first_number * second_number)
elif choice == 4:
    print(first_number, "/", second_number, "=", first_number / second_number)
