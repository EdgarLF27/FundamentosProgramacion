def numeros0():
    numeros = int(input("Introduce cuántos números debe solicitar el programa: "))
    contador_mayor0 = 0
    contador_menor0 = 0
    contador_igual0 = 0 #inicializamos los contadores en 0

    for i in range(numeros):
        num = int(input("Introduce un número: "))
        
        if num > 0:
            contador_mayor0 += 1
        elif num < 0:
            contador_menor0 += 1
        elif num == 0:
            contador_igual0 += 1
            
    print(f"La cantidad de números mayores que 0 es: {contador_mayor0}")
    print(f"La cantidad de números menores que 0 es: {contador_menor0}")
    print(f"La cantidad de números iguales a 0 es: {contador_igual0}")

numeros0()