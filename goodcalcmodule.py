print("||Four Function Calculator||")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

def choice_parameter():
    while True:
        choice = input("|Enter Choice|--> 1 | 2 | 3 | 4 : ")
        if choice not in [1, 2, 3, 4]:
            print("Invalid Input. Try Again?")
        return choice
        
choice_parameter()

def addition (x, y):
    return x + y

def Subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

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
