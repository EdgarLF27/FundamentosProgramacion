import random
def promedio():
    contador = 0
    acumulador = 0 #se inicializan en 0

    while contador < 10: #se repite 10 veces
        numero = random.randint(1, 100) #se genera un número aleatorio entre 1 y 100
        contador += 1 #se agrega un 1 al contador hasta llegar a 10
        acumulador += numero #se suma el número aleatorio al acumulador

    promedio = acumulador / contador
    print(f"El promedio de los 10 números es : {promedio}") #se imprime el promedio de los 10 números
    print(f"La suma de los números fue : {contador}") #se imprime la suma de los 10 números

promedio()