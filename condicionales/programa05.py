'''
Programa que pide un nombre de usuario y una contraseña
Si el usuario es "pepe" y la contraseña es "asdasd" se indica que se ha accedido al sistema
si no, se niega el acceso
Enrada: user, password
Salida: Accediste/No accediste al sistema
'''

correct_user: str = "pepe"
correct_password: str = "asdasd"
user = str(input("Introduce el usuario: "))
password = str(input("Introduce la contraseña: "))

if user == correct_user and password == correct_password:
    print("Accediste al sistema")
else:
    print("No accediste al sistema")