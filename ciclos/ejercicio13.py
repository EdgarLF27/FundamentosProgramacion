def calcular_pagos():
    meses = 20
    total_pagado = 0
    pagos_mensuales = []

    for mes in range(1, meses + 1):
        pago = 10 * (2 ** (mes - 1))  # Calcular el pago del mes
        pagos_mensuales.append(pago)  # Agregar el pago a la lista
        total_pagado += pago  # Sumar al total pagado

    # Mostrar los pagos mensuales
    for mes, pago in enumerate(pagos_mensuales, start=1):
        print(f"Mes {mes}: {pago} euros")

    # Mostrar el total pagado
    print(f"Total pagado después de {meses} meses: {total_pagado} euros")

calcular_pagos()