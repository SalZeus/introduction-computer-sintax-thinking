#basic mathematical operations (added functions for ease of writing)

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

#area of a triangle, why is it important to properly name variables


base = 2
altura = 4

area = (base*altura) /2

print("tu triangulo tiene un area de " + str(int(area)))

#string array management

my_string = "Platzi"

print(len(my_string))
#position logic
print(my_string[0])
print(my_string[1])
print(my_string[2])
#initial to end
print(my_string[2:])
#end is not inclusive without an initial number!
print(my_string[:3])
#last 2
print(my_string[:-2])
#two steps at a time
print(my_string[::2])
#usual string concatenation
print("Yo amo a " +my_string)
#saving one Bart at a time (he loves Platzi it seems)
print(("Yo amo a "+my_string+", ") *10)

#variable concatenation formats with array position formats [initial, final, steps](slicing)

nombre = str(input("Tu nombre: "))
print("Tu nombre es "+str(nombre))

numero = float(input("Escribe un numero: "))
print("tu numero es "+str(numero))

print(f"tu numero es {numero}")

#boolean results

print(2==3)
print(2!=3)
print(2<3)
print(2>3)
print(2<=3)
print(2>=3)

#basic "if" statements
num_1 = int(input("escoge un numbero(sin decimales): "))
num_2 = int(input("Escoge otro numero(sin decimales): "))

if num_1>num_2:
    print("el primer numero es mayor que el segundo")
elif num_1 < num_2:
    print("el segundo numero es mayor que el primero")
else:
    print("Los dos numeros son iguales")

#exercise, based on previous information

print("Wen dia, hoy te ayudare(como la benevolente compu que soy) a saber quien es más anciano o menos anciano entre dos personas!")
print("Por favor, sigue las instrucciones debajo y asegurate de seguirlas!")
nombre1 = str(input("Dame el nombre de la primera persona: "))
edad1 = int(input("Que edad tiene " +str(nombre1)+"? "))
nombre2 = str(input("Dame el nombre de la segunda persona: "))
edad2 = int(input("Que edad tiene " +str(nombre2)+"? "))
print("*procesa a velocidad de la luz")

def comparacionEdad(nombre1, edad1, nombre2, edad2):
    if edad1>edad2:
        print(f"parece que {nombre1} tiene {int(edad1) - int(edad2)} años mas que {nombre2}")
    elif edad1<edad2:
        print(f"parece que {nombre2} tiene {int(edad2) - int(edad1)} años mas que {nombre1}")
    else:
        print(f"No mamen, {nombre1} y {nombre2} tienen la misma edad ({edad1}) alv, no me necesitan para esto :s")

comparacionEdad(nombre1, edad1, nombre2, edad2)

