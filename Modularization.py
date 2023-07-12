#out of class exercise
#choosing

def choose():
    print("""Es hora de hallar una raiz cuadrada, pero como lo haremos esta vez?🤔
          1. Enumeracion exhaustiva 
          2. aproximación de soluciones 
          3. Búsqueda binaria.""")
    option = int(input("escribe 1(enumeración exhaustiva), 2(aproximación de soluciones) o 3(búsqueda binaria): "))
    number = int(input("escribe el numero al cual le quieres hallar la raiz: "))

    if option == 1:
        enumeration(number)
    elif option == 2:
        approximation(number)
    elif option == 3:
        binarySearch(number)
    else:
        print("asegurate de poner 1, 2 o 3, sin espacios u otros caracteres")
        choose()


#enumaration 
def enumeration(objective):
    answer = 0
    while answer **2 < objective:
        answer += 1

    if answer ** 2 == objective:
        print(f"La raiz cuadrada de {objective} es {answer}")
    else:
        print(f"{objective} no tiene una raiz cuadrada exacta")

#approximation
def approximation(objective):
    epsilon = 0.001
    step =  epsilon**2
    answer = 0.0

    while abs(answer**2 - objective) >= epsilon and answer <= objective:
        answer += step
    if abs(answer**2 - objective) >= epsilon:
        print(f"No se encontro la raiz cuadrada del objective")
    else:
        print(f"La raiz cuadrada de {objective} es {answer}")

#binary searching
def binarySearch(objective):
    epsilon = 0.0001
    low = 0.0
    high = max(1.0, objective)
    answer = (high + low / 2)
    while abs(answer**2 - objective) >= epsilon:
        if answer ** 2 < objective:
            low = answer
        else:
            high = answer
        
        answer = (high+low) / 2

    print(f"La Raiz cuadrada de {objective} es {answer}")

choose();