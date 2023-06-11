contador_pares = 0
contador_impares = 0
sumatoria_pares = 0

for i in range(4):
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        contador_pares += 1
        sumatoria_pares += n
    else:
        contador_impares += 1

print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)
print("Sumatoria de números pares:", sumatoria_pares)
