def factorial(number):
    """
    Calcula el factorial de number int > 0
    returns number!"""
    print(number)
    if number == 1:
        return 1
    
    return number * factorial(number - 1)

number = int(input("escribe un entero: "))

print(factorial(number))