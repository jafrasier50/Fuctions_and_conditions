print("Fizz Buzz Divisibility! Divisible by 3? FIZZ! Divisible by 5? BUZZ! Divisible by both? FIZZ BUZZ!")

number = int(input("FizzBuzz your input here: "))

def divisibility():
    if number % 15 == 0:
        print("FIZZBUZZ!!!")
    elif number % 3 == 0:
        print("FIZZ!")
    elif number % 5 == 0:
        print("BUZZ!")
    else:
        print("WHOOPS! That number isn't a fizz or buzz! Try again next time.")
        return number
divisibility()
