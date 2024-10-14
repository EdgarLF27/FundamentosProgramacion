import math

x1 = float(input("Introduce la coordenada x1: "))
y1 = float(input("Introduce la coordenada y1: "))
x2 = float(input("Introduce la coordenada x2: "))
y2 = float(input("Introduce la coordenada y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"La distancia entre los puntos es: {distancia:.2f}")
