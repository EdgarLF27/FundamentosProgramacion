p1 = float(input("Ingresa la calificación del primer parcial "))
p2 = float(input("Ingresa la calificación del segundo parcial "))
p3 = float(input("Ingresa la califcación del calificación parcial "))
exam = float(input("Ingresa la calificación del examen "))
trab = float(input("Ingresa la calificación del trabajo final "))
parciales = p1 + p2 + p3
final = 0.55 * parciales  + 0.3 * exam + 0.15 * trab
print("Tu calificación final es: ", final)
