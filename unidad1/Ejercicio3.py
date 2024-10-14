'''
Programa que solicita al usuario los catetos de un triángulo rectángulo y calcula la hipotenusa
Entrada -> Cateto a y b
Salida -> "La hipotenusa es: hipotenusa"
'''
import math
a = int(input ("Escribe el valor del cateto A: "))
b= int(input("Escribe el valor del cateto B: "))
c = (a * a + b * b) ** (1/2)
c = math.sqrt (a * 2 + b **b)
print ("El valor de la hipotenusa es : ", c)