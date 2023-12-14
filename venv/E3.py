"""
Marc Guerra Hernandez
14/12/2023
Examen pp2
"""
filas = 8
columnas = 8

posicion1 = input("Dame una posición: ")
posicion2 = input("Dame otra posición: ")

for fila in range(filas):
    for columna in range(columnas):
        blanca = (fila + columna) % 2 == 0
        if blanca:
            print('B', end=' ')
        else:
            print('N', end=' ')
    print()
