"""
N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros.
"""

atletas = []
marcas = []


def peticionDatos():
    print(f" Si desea dejar de agregar atletas escriba 'ok'")
    i = 1
    record = 15.5
    while i != 0:
        nombre = input(f"\n Ingrese el nombre del atleta: ")
        atletas.append(nombre)
        if nombre == "ok":
            i = 0
            atletas.remove("ok")
            # print(f"\n{atletas} and {marcas}")       
        if i != 0:
            marca = float(input(f"\n Ingrese la marca del deportista: "))
            marcas.append(marca)

    union = list(zip(atletas,marcas))
    union = sorted(union, key=lambda union: union[1], reverse=True)

    print(f"\n Felicidades, {union[0][0]}, haz ganado la medalla de oro. Tu marca fue de {union[0][1]} metros!")
    if union[0][1] >= record:
        print(f"\n Además haz roto el anterior record mundial, el pago será de 500millones\n")
    
    # print(f"\n Este atleta ha roto el record mundial, el pago será de 500millones :) \n")

    
peticionDatos()



