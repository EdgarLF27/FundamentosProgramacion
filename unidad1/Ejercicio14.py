'''
Programa que pide un número de dos cifras y lo invierte
Entrada -> numero
Salida -> "El número invertido es: numero_invertido"
'''
numero = int(input("Introduce un número de dos cifras: "))

decenas = numero // 10  
unidades = numero % 10 

numero_invertido = (unidades * 10) + decenas

print(f"El número invertido es: {numero_invertido}")
