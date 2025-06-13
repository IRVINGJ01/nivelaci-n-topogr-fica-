print("Calculadora de calorías")
Proteina =float(input("¿Cuantos gramos de Proteina comiste? "))
Carbohidratos =float(input("¿Cuantos gramos de Carbohidratos comiste? "))
Grasas =float(input("¿Cuantos gramos de Grasas comiste? "))

#Calculo de calorias
calorias_totales = (Proteina * 4) + (Carbohidratos * 4) + (Grasas * 9)

#Mostrar resultado
print(f"\nTotal aproximado de calorias {calorias_totales} kcal")

#Evaluar si estas dentro del limite
if calorias_totales > 1700:
    print(" Te pasaste del limite diario de 1700 kcal! ")

else:
    print("vas bien con tus calorias. ")

#Guardar archivo de texto
with open ("registro_comida.txt", "a") as archivo:
    archivo.write(f"Proteina: {Proteina} g, Carbohidratos {Carbohidratos} g, Grasas {Grasas} g, Total: {calorias_totales} kcal\n")