contador_mayores = 0
contador_menores = 0
maximo = float('-inf')
minimo = float('inf')

for i in range(10):
    numero = int(input("Ingrese un número: "))
    if numero > 100:
        contador_mayores += 1
    elif numero < 100:
        contador_menores += 1

    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

print("Cantidad de números mayores a 100:", contador_mayores)
print("Cantidad de números menores a 100:", contador_menores)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)
