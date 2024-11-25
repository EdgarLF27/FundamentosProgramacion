# Solicitar al usuario un número entero
try:
    numero = int(input("Por favor, ingresa un número entero: "))
    
    # Convertir el número a binario
    binario = bin(numero)
    
    # Si deseas mostrar solo la parte binaria sin el prefijo '0b', ya que la funcion bin devuelve el numero en binario con el prefijo
    print(f"El número {numero} en binario (sin prefijo) es: {binario[2:]}")
    
except ValueError:
    print("Por favor, ingresa un número entero válido.")