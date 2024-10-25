'''
Programa que pide dos números, "nota" y "edad" y un caracter "sexo"
Muestra el mensaje "Aceptado" si la nota es mayor o igual a 5, la edad es mayor o igual a 18 y el sexo es "F"
En caso de que se cumpla lo mismo pero el sexo sea "M" se muestra "Posible"
Si no se cumplen las condiciones se muestra "No aceptad@"
'''
nota =  int(input("Introduce tu nota: "))
edad = int(input("Introduce tu edad: "))
sexo = input("Introduce tu sexo (F/M): ")

if nota >= 5 and edad >= 18 and sexo == "F":
    print("Aceptado")
elif nota >= 5 and edad >= 18 and sexo == "M":
        print("Posible")
else:
            print("No aceptado")