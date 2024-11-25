def verificar_vocales():
    while True:  # Bucle infinito
        caracter = input("Introduce un carácter (o un espacio para terminar): ")  # Solicita un carácter

        if caracter == " ":  # Verifica si el carácter es un espacio
            print("Programa terminado.")
            break  # Sale del bucle si se introduce un espacio

        # Verifica si el carácter es una vocal
        if caracter.lower() in 'aeiouáéíóú':
            print("VOCAL")
        else:
            print("NO VOCAL")

verificar_vocales()