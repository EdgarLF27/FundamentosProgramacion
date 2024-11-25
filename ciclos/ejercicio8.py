def pares():
    print ("Introduce 2 números para mostrarte los números pares que hay entre estos")
    num1 = int(input("Introduce el primer numero"))
    num2 = int(input("Introduce el segundo numero"))

    menor = min(num1, num2)
    mayor = max(num1, num2)
    for i in range (num1, num2):
        if i % 2 == 0:
          print (i)
      
pares()