'''
Programa que pide un numero y diga si es positivo, negativo o 0
Entrada: numero
Salida: positivo/negativo/0
'''
n = int(input("Introduce un numero: "))

if n > 0:
    print(f"El numero {n} es positivo")
elif n < 0:
    print(f"El numero {n} es negativo")
elif n == 0:
    print(f"El numero {n} es 0")