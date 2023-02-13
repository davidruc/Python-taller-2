listaCampus = []

def crearLista ():   
    print("menu")
    i = 1
    while i != 0:
        estudiante = input("Ingrese nombre: ")
        listaCampus.append(estudiante)
        if estudiante == "3":
            i = 0
            

crearLista()