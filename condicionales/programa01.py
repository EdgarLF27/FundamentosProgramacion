'''
Programa que pide dos números, indique cual es menor y cual es mayor y si los dos son iguales que se muestre el mensaje "son iguales"

entrada: n1, n2
salida: menor, mayor y/o iguales
'''
n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))

if n1 > n2:
    print(f"El número {n1} es mayor que {n2}")

elif n1 < n2:
    print(f"El número {n2} es mayor que {n1}")
elif n1 == n2:
        print("Los números son iguales")
        