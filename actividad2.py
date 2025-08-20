import math 
a = float(input("ingresa la altura: "))
b = float(input("ingresa la base: "))
area_triangulo = ((b*a)/2)
print(area_triangulo)

#----------Actividad 3---------------
exit = "SI"
while exit == "SI":
    precio = float(input("ingrese un precio: "))
    if(precio>0):
        print("el precio es valido")
    else:
        print("el precio no es valido")
    exit = input("Desea continuar? [SI][NO]")


