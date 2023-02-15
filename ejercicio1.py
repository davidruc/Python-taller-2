listaCampus = []
listaCampusSputnik = []

def crearLista ():   
    print("\n Creador de lista de estudiantes Artemis! \n (Para dejar de ingresar nombres escriba:  ok ) \n")
    i = 1
    while i != 0:
        estudiante = input("Ingrese el nombre del estudiante: ")
        listaCampus.append(estudiante)   
        if estudiante == "ok":
            i = 0
            listaCampus.remove("ok")
            print(f"\n{listaCampus}")
        
def crearListaSputnik ():   
    print("\n Creador de lista de estudiantes Sputnik! \n\n Para dejar de ingresar nombres escriba: \t ok \n")
    i = 1
    while i != 0:
        estudiante = input("Ingrese el nombre del estudiante: ")
        listaCampusSputnik.append(estudiante)  
        if estudiante == "ok":
            i = 0
            listaCampusSputnik.remove("ok")
            print(f"\n{listaCampusSputnik}")

def listadoCampers():
    print(f"\n Listado de estudiantes Artemis: ")
    for x in listaCampus:
        print(x)

def listadoCampersSputnik():
    print(f"\n Listado de estudiantes Sputnik: ")
    for x in listaCampusSputnik:
        print(x)


def agregarCamper ():
    respuesta=input(f"\n Desea agregar otro estudiante a la lista de Artemis?: ( si / no ): ")
    while respuesta == "si":
        
        estudiante = input(f"\n ingrese el nombre del estudiante: ")
        listaCampus.append(estudiante)
        respuesta=input(f"\n Desea agregar otro estudiante a la lista de Artemis?: ( si / no ): ")
        print(f"Nueva lista: \n {listaCampus}")
        

def agregarCamperSputnik ():
    respuesta=input(f"\n Desea agregar otro estudiante a la lista de Sputnik?: ( si / no ): ")
    while respuesta == "si":
        
        estudiante = input(f"ingrese el nombre del estudiante: ")
        listaCampusSputnik.append(estudiante)
        respuesta=input(f"\n Desea agregar otro estudiante a la lista de Sputnik?: ( si / no ): ")
        print(f"Nueva lista: \n {listaCampusSputnik}")


def eliminadorCampers():
    print(listaCampus)
    eliminacion = input(f"\n Qué camper deseas eliminar de Artemis?: ")
    listaCampus.remove(eliminacion)
    print(f"Nueva lista: \n {listaCampus}")


def eliminadorCampersSputnik():
    print(listaCampusSputnik)
    eliminacion = input(f"\n Qué camper deseas eliminar de Sputnik?: ")
    listaCampusSputnik.remove(eliminacion)
    print(f"Nueva lista: \n {listaCampusSputnik}")
       

def ordenadorDeLista():
   
    listaCampus.sort()
    print(f"\n Esta es la lista en orden alfabetico: \n {listaCampus}")


def ordenadorDeListaSputnik():
   
    listaCampusSputnik.sort()
    print(f"\n Esta es la lista en orden alfabetico: \n {listaCampusSputnik}")


def buscarCamper ():
    print(listaCampus)
    estudiante= input(f"\n ingrese el estudiante del cuál desea hacer la búsqueda: ")
    posicion= listaCampus.index(estudiante)
    print(f"Su estudiante {estudiante} es el número {1+posicion} de la lista.")

def buscarCamperSputnik ():
    print(listaCampusSputnik)
    estudiante= input(f"\n ingrese el estudiante del cuál desea hacer la búsqueda: ")
    posicion= listaCampusSputnik.index(estudiante)
    print(f"Su estudiante {estudiante} es el número {1+posicion} de la lista.")

print(f"-------------------------MENU--------------------------------\n 1.  CREAR GRUPO ARTEMIS: \n 1.1 LISTAR CAMPERS DE ARTEMIS \n 1.2 AGREGAR CAMPERS A ARTEMIS \n 1.3 ELIMINAR CAMPERS DE ARTEMIS \n 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS \n 1.5 BUSCAR CAMPEREN LISTA DE ARTEMIS \n 2.  CREAR GRUPO SPUTNIK: \n 2.1 LISTAR CAMPERS DE SPUTNIK \n 2.2 AGREGAR CAMPERS A SPUTNIK \n 2.3 ELIMINAR CAMPERS DE SPUTNIK \n 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK \n 2.5 BUSCAR CAMPEREN LISTA DE SPUTNIK")



respuesta = 5
while respuesta != 3:
    respuesta = float(input(f"Digite opción: "))

    if respuesta == 1.0:
        crearLista ()

    elif respuesta == 1.1:
        listadoCampers()

    elif respuesta == 1.2:
        agregarCamper()

    elif respuesta == 1.3:
        eliminadorCampers()

    elif respuesta == 1.4:
        ordenadorDeLista()

    elif respuesta == 1.5:
        buscarCamper()

    elif respuesta == 2.0:
        crearListaSputnik ()
        
    elif respuesta == 2.1:
        listadoCampersSputnik()

    elif respuesta == 2.2:
        agregarCamperSputnik()

    elif respuesta == 2.3:
        eliminadorCampersSputnik()

    elif respuesta == 2.4:
        ordenadorDeListaSputnik()

    elif respuesta == 2.5:
        buscarCamperSputnik()

    elif respuesta != 3:
        print("Ingresa porfavor un valor válido!")
        
    