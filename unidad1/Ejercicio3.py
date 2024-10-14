import math
a = int(input ("Escribe el valor del cateto A: "))
b= int(input("Escribe el valor del cateto B: "))
c = (a * a + b * b) ** (1/2)
c = math.sqrt (a ** 2 + b ** 2)
print ("El valor de la hipotenusa es : ", c)