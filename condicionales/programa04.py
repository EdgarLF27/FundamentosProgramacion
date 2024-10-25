'''
Programa que pide al usuario dos numeros y muestra su division
Entrada: n1, n2
Salida: division/advertencia si el segundo numero es 0
'''

n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))

if n2 == 0:
    print("No se puede realizar una division entre 0")
else:
    print(f"El resultado de la division es {n1/n2}")