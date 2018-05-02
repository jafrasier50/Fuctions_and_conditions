#assignment 2

number = int(input("Please input your number here: "))

def even_or_odd():
    if number % 2 == 0:
        print("Even!")
    else:
        print("Odd!")
        return number

even_or_odd()
