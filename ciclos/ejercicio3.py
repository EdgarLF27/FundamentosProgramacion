def contadoryacumulador():
    acumulador = 0
    contador = 0 #inciciar ambos en 0
     
    while True:
        #pedir al usuario un numero 
        numero = int(input("Ingresa un número (0 si quieres terminar) y la computadora sumara todos"))
        if numero == 0:
            break
        acumulador += numero
        contador += 1
        if contador > 0: #verificar si se han introducido valores
            media = acumulador / contador 
            print (f"Suma: {acumulador}")
            print (f"Media: {media}")
        else:
            print("No se introdujeron números")
            #llamar a la funcion
        contadoryacumulador()