num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor = max(num1, num2, num3)

print("El número mayor es:", mayor)

if mayor % 2 == 0:
    print("El número mayor es par")
else:
    print("El número mayor es impar")
