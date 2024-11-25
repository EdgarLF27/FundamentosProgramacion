def tablas():
    for i in range (1, 6): #iterar del 1 al 5
        print (f"Tabla de multiplicar del {i}:")
        for j in range (1, 11): #multiplicar del 1 al 10
            resultado = i * j
            print (f"{i} x {j} = {resultado}")
            print () #salto de linea
tablas()