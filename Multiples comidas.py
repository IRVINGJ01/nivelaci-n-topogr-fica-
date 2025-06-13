
from datetime import datetime

print("Registro de varias comidas")
cantidad = int(input("¿cuantas comidas vas a registrar hoy? "))

total_calorias_dia = 0
registro = []

for i in range(cantidad):
    print(f"\n---Comida {i+1} ---")
    proteina = float(input("Gramos de proteina: "))
    carbohidratos =float(input("Gramos de carbohidratos: "))
    grasas = float(input("Gramos de grasas: "))

    calorias = (proteina * 4) + (carbohidratos * 4) + (grasas * 9)
    total_calorias_dia += calorias

    registro.append((f"Comida {i+1}: Proteina {proteina}g, Carbohidratos{carbohidratos}g, Grasas{grasas}g, Total: {calorias:.2f} kcal"))

print("\n Registro del dia:")
for linea in registro:
    print(linea)

print(f"\n Total de calorias del dia: {total_calorias_dia:.2f} kcal")

#Guardar en archivo
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("registro_comidas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"\n\n{fecha} - Registro diario\n")
    for linea in registro:
        archivo.write(linea + "\n")
    archivo.write(f"Totao de calorias: {total_calorias_dia:.2f} kcal\n")




