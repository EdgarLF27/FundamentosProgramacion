'''
Programa que solicita la temperatura en grados Fahrenheit y la convierte a grados Celsius
Entrada -> grados Fahrenheit
Salida -> grados Celsius
'''
fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
r = (fahrenheit - 32) 
c = (r * 5) / 9
print ("La temperatura en grados Celsius es: ", c)