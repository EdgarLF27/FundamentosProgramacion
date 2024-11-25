import random

def adivina_el_numero():
    # Generar un número aleatorio del 1 al 100
    numero_a_adivinar = random.randint(1, 100)
    intentos_restantes = 10

    print("Adivina el número que he pensado entre 1 y 100.")
    print(f"Tienes {intentos_restantes} intentos para adivinarlo.")

    for intento in range(1, 11):  # 10 intentos
        try:
            # Solicitar al usuario que ingrese un número
            adivinado = int(input(f"Intento {intento}: Introduce tu número: "))

            # Comparar el número introducido con el número a adivinar
            if adivinado < numero_a_adivinar:
                print("El número a adivinar es mayor.")
            elif adivinado > numero_a_adivinar:
                print("El número a adivinar es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_a_adivinar} en {intento} intentos.")
                break  # Salir del ciclo si se adivina el número

            # Restar un intento
            intentos_restantes -= 1
            print(f"Te quedan {intentos_restantes} intentos.")
            
            if intentos_restantes == 0:
                print(f"Lo siento, has agotado tus intentos. El número era {numero_a_adivinar}.")

        except ValueError:
            print("Por favor, introduce un número entero válido.")

# Llamar a la función para iniciar el juego
adivina_el_numero()