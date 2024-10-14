'''
Programa que solicita el precio de un producto y le aplica un descuento del 15%
Entrada -> precio
Salida -> Precio del producto con el descuento aplicado
'''
p = float(input("Ingresa el precio del producto "))
desc = p * 15/100
total = p - desc
print ("Pagaras por tu producto: ", total)