'''
Programa que solicita dos numeros y los intercambia
Entrada -> a, b
Salida -> "Despues del intercambio, A vale: b, y B vale: a"

'''
A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

A, B = B, A

print(f"Después del intercambio, A vale: {A}")
print(f"Después del intercambio, B vale: {B}")
