def es_primo(num):
    """Función que determina si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mostrar_primos(n):
    """Función que muestra los primeros n números primos."""
    primos_encontrados = []
    numero = 2  # El primer número primo

    while len(primos_encontrados) < n:
        if es_primo(numero):
            primos_encontrados.append(numero)
        numero += 1

    return primos_encontrados

# Solicitar al usuario la cantidad de números primos a mostrar
try:
    cantidad = int(input("¿Cuántos números primos deseas mostrar? "))
    if cantidad <= 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        primos = mostrar_primos(cantidad)
        print(f"Los primeros {cantidad} números primos son: {primos}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")