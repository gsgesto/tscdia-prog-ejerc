importe = float(input("Ingrese el importe a pagar: "))
forma_pago = input("Seleccione la forma de pago (1 para Contado, 2 para Tarjeta, 3 para Débito): ")

imp = "Importe: $"
desc = "Descuento: $"
int = "Interés: $"
imp_total = "Importe total: $"

if forma_pago == "1":
    descuento = importe * 0.10
    importe_total = importe - descuento
    print(imp, importe)
    print(desc, descuento)
    print(imp_total, importe_total)
elif forma_pago == "2":
    interes = importe * 0.10
    importe_total = importe + interes
    print(imp, importe)
    print(int, interes)
    print(imp_total, importe_total)
elif forma_pago == "3":
    descuento = importe * 0.05
    importe_total = importe - descuento
    print(imp, importe)
    print(desc, descuento)
    print(imp_total, importe_total)
else:
    print("Forma de pago inválida")
