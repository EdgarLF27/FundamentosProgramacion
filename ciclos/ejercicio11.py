import math

def es_primo(numero):
    # Verificar si el número es menor o igual a 1
    if numero <= 1:
        return False
    # Verificar si el número es 2 o 3
    if numero <= 3:
        return True
    # Si el número es par y mayor que 2, no es primo
    if numero % 2 == 0:
        return False
    
    # Verificar divisibilidad desde 3 hasta la raíz cuadrada del número
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
            
    return True

def primo():
    # Solicitar al usuario que introduzca un número
    numero = int(input("Introduce un número entero: "))
    
    # Verificar si el número es primo
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

# funcion principal
primo()