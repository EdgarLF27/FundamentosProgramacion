def calcular_potencia(base, exponente):
    resultado = 1.0  # Inicializar el resultado en 1
    for _ in range(exponente):  # Repetir exponente veces
        resultado *= base  # Multiplicar el resultado por la base
    return resultado

def exp():
    # Solicitar al usuario que ingrese la base y el exponente
    base = float(input("Introduce un número real (base): "))
    exponente = int(input("Introduce un número entero positivo (exponente): "))

    # Verificar que el exponente sea positivo
    if exponente < 0:
        print("El exponente debe ser un número entero positivo.")
        return

    # Calcular la potencia
    resultado = calcular_potencia(base, exponente)

    # Mostrar el resultado
    print(f"{base} elevado a {exponente} es: {resultado}")

exp()