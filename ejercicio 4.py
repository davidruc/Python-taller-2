"""
Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general.
"""

almacen = []
articulo = []
NoVentas = []
sumaunidades = []

def funcionArticulomasVendido ():
    no = int(input(f"Cuantos almacenes desea ingresar?: "))
    for i in range(no):
        almacenes = input(f"\n Ingrese el nombre del almacén: ")
        almacen.extend([almacenes]*5)
        z = 0
        print(almacen)
        sumaunidade = 0
        while z != 5:
            for e in range(1):
                articulos = input(f"\n Ingrese el artículo: ")
                articulo.append(articulos)            
            for x in range(1):
                ventas = int(input(f"\n Ingrese el número de unidades vendidas:"))
                NoVentas.append(ventas)
                sumaunidade += ventas
            sumaunidades.extend([sumaunidade]*5)                   
            z += 1
    union =  list(zip(almacen,articulo,NoVentas))
    union = sorted(union, key=lambda union: union[2], reverse=True) 
    print(f"\n El almacen {union[0][0]} vendió la mayor cantidad de unidades de un artículo ({union[0][2]} veces), con el producto {union[0][1]}.\n")
    union2 = list(zip(almacen,articulo,NoVentas, sumaunidades ))
    union2 = sorted(union2, key=lambda union2: union2[3], reverse=True) 
    print(f"El almacen {union2[0][0]} fue el que más vendió más artículos \n")
    newlist = []
    for j in range(4):
        newlist += union2[j]
    print(f"y su producto estrella fue {newlist[1]}")
funcionArticulomasVendido()