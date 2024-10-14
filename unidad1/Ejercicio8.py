base = float(input("Ingresa tu sueldo base "))
v1 = float(input("Ingresa el valor de la venta 1 "))
v2 = float(input("Ingresa el valor de la venta 2 "))
v3 = float(input("Ingresa el valor de la venta 3 "))
r1 = v1 *  10/100
r2 = v2 *  10/100
r3 = v3 *  10/100
comision =  r1 + r2 + r3
total = base + comision
print ("Tu sueldo total es: ", total)