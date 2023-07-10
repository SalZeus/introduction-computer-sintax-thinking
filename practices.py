def sum(num1, num2):

    resultado = num1 + num2;
    return resultado

def difference(num1, num2):

    resultado = num1 - num2;
    return resultado

def product(num1, num2):

    resultado = num1 * num2;
    return resultado

def divisionNoRemainder(num1, num2):

    resultado = num1 // num2;
    return resultado

def decimalDivision(num1, num2):

    resultado = num1 / num2;
    return resultado

def divisonRemainder(num1, num2):

    resultado = num1 % num2;
    return resultado

def exponent(num1, num2):

    resultado = num1 ** num2;
    return resultado

print(sum(1, 2))
print(difference(2, 5))
print(product(2.0, 3))
print(divisionNoRemainder(6, 2))
print(decimalDivision(6, 4))
print(divisonRemainder(7, 2))
print(exponent(2, 3))


base = 2
altura = 4

area = (base*altura) /2

print("tu triangulo tiene un area de " + str(int(area)))

my_string = "Platzi"

print(len(my_string))
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[2:])
print(my_string[:3])
print(my_string[:-2])
print(my_string[::2])
print("Yo amo a " +my_string)
print(("Yo amo a "+my_string+", ") *10)

nombre = input(str("Tu nombre: "))
print("Tu nombre es "+nombre)

numero = float(input("Escribe un numero: "))
print("tu numero es "+numero)

