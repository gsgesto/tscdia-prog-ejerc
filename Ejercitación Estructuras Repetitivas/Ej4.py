sumatoria_positivos = 0

for i in range(10):
    n = float(input("Ingrese un número: "))
    if n > 0:
        print(n)
        sumatoria_positivos += n

print("Sumatoria de números positivos:", sumatoria_positivos)
