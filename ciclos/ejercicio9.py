def intervalo_numeros():
    # Pedir límites del intervalo
    while True:
        limite_inferior = float(input("Introduce el límite inferior del intervalo: "))
        limite_superior = float(input("Introduce el límite superior del intervalo: "))
        
        if limite_inferior < limite_superior:
            break  # Salir del bucle si los límites son válidos
        else:
            print("El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")

    suma_intervalo = 0
    fuera_intervalo = 0
    limite_inferior_igual = False
    limite_superior_igual = False

    print("Introduce números (introduce 0 para terminar):")
    
    while True:
        numero = float(input())
        
        if numero == 0:
            break  # Terminar si se introduce 0
        
        # Verificar si el número está dentro del intervalo
        if limite_inferior < numero < limite_superior:
            suma_intervalo += numero
        else:
            fuera_intervalo += 1
        
        # Verificar si el número es igual a los límites
        if numero == limite_inferior:
            limite_inferior_igual = True
        if numero == limite_superior:
            limite_superior_igual = True

    # Resultados
    print(f"La suma de los números dentro del intervalo ({limite_inferior}, {limite_superior}) es: {suma_intervalo}")
    print(f"Números fuera del intervalo: {fuera_intervalo}")
    if limite_inferior_igual:
        print("Se introdujo un número igual al límite inferior.")
    if limite_superior_igual:
        print("Se introdujo un número igual al límite superior.")

intervalo_numeros()