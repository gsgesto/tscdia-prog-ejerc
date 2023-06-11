opcion = input("Seleccione el tipo de cambio (1 para pesos a dólares, 2 para dólares a pesos): ")
monto = float(input("Ingrese el monto a convertir: "))

if opcion == "1":
    tipo_de_cambio = float(input("Ingrese el tipo de cambio de pesos a dólares: "))
    conversion = monto / tipo_de_cambio
    print("El monto en dólares es:", conversion)
elif opcion == "2":
    tipo_de_cambio = float(input("Ingrese el tipo de cambio de dólares a pesos: "))
    conversion = monto * tipo_de_cambio
    print("El monto en pesos es:", conversion)
else:
    print("Opción inválida")
