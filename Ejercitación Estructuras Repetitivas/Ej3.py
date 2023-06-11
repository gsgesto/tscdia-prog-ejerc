contador_mujeres = 0
contador_varones = 0
contador_mayores = 0
contador_menores = 0

for i in range(15):
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M para mujer, V para varón): ")

    if sexo == "M":
        contador_mujeres += 1
    elif sexo == "V":
        contador_varones += 1

    if edad >= 18:
        contador_mayores += 1
    else:
        contador_menores += 1

print("Cantidad de mujeres:", contador_mujeres)
print("Cantidad de varones:", contador_varones)
print("Cantidad de mayores de edad:", contador_mayores)
print("Cantidad de menores de edad:", contador_menores)
