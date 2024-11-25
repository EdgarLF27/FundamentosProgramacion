def ahorros():
    # Crear una lista para almacenar los ahorros de cada mes
    ahorros_mensuales = []

    # Solicitar al usuario que ingrese los ahorros de cada mes
    for mes in ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]:
        ahorro = int(input(f"¿Cuánto ahorraste en {mes}? "))
        ahorros_mensuales.append(ahorro)  # Agregar el ahorro a la lista

    # Imprimir los ahorros de cada mes
    for i, mes in enumerate(["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]):
        print(f"En {mes} ahorraste: {ahorros_mensuales[i]}")

    # Calcular y mostrar el total ahorrado
    total_ahorrado = sum(ahorros_mensuales)
    print(f"Total ahorrado en el año: {total_ahorrado}")

ahorros()