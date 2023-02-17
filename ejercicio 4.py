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
        almacen.extend([almacenes]*4)
        almacen.append(almacenes)
        z = 0
        while z != 5:
            sumaunidades = 0
            for x in range(1):
                articulos = input(f"\n Ingrese el artículo: ")
                articulo.append(articulos)
            
            for y in range(1):
                ventas = int(input(f"\n Ingrese el número de unidades vendidas:"))
                NoVentas.append(ventas)
                sumaunidades += ventas
                sumaunidades.append(sumaunidades)
            
            # sumaunidades.extend([ventas]*4)
            
                
            z += 1
    union =  list(zip(almacen,articulo,NoVentas,ventas))
    union = sorted(union, key=lambda union: union[2], reverse=True)  
    print(f"\n El almacen {union[0][0]} vendió la mayor cantidad de unidades de un artículo. El producto {union[0][1]} fue vendido {union[0][2]} veces.\n")
    union = sorted(union, key=lambda union: union[3], reverse=True) 

funcionArticulomasVendido()

# def funcionAlmacenqmasvendio():

