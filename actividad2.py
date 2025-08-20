# import math 
# a = input("ingresa la altura: ")
# astring = float(a)
# b = input("ingresa la base: ")
# bstring = float(b)
# area_triangulo = ((bstring*astring)/2)
# print(area_triangulo)

#----------Actividad 3---------------
exit = "SI"
while exit == "SI":
    precio = float(input("ingrese un precio: "))
    if(precio>0):
        print("el precio es valido")
    else:
        print("el precio no es valido")
    exit = input("Desea continuar? [SI][NO]")


