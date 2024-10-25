'''
Programa que pide un número y dice si es par o impar
Enterda: numero
Salida: par/impar
'''
n = int(input("Introduce un numero: "))

if n % 2 == 0:
    print(f"El numero {n} es par")
else:
    print(f"El numero {n} es impar")