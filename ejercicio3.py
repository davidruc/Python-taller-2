"""
3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos.
"""

def valorAPagar ():
    SueldoKm = float(input(f"ingrese el sueldo básico por kilometro del deportista: "))
    noKmrecorridos = float(input(f"¿Cuál fue el número de kilometros recorridos por el deportista durante toda la vuelta? "))
    camisetalider = float(input(f"¿Cuantos kilometros fue lider?: "))
    
    if camisetalider >= 1800:
        calculo = SueldoKm*(noKmrecorridos-camisetalider) + camisetalider*SueldoKm*1.25 
    else:
        calculo = SueldoKm*noKmrecorridos
    print(calculo)
    
valorAPagar()