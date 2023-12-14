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

letras_validas = 'abcdefgh'
letra1, letra2 = posicion1[0].lower(), posicion2[0].lower()

if letra1 in letras_validas and letra2 in letras_validas:
    fila1, columna1 = int(posicion1[1]) - 1, -1
    fila2, columna2 = int(posicion2[1]) - 1, -1

    for i in range(len(letras_validas)):
        if letra1 == letras_validas[i]:
            columna1 = i
        if letra2 == letras_validas[i]:
            columna2 = i

    for fila in range(filas):
        for columna in range(columnas):
            if fila == fila1 and columna == columna1:
                print('#', end=' ')
            elif fila == fila2 and columna == columna2:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()
else:
    print("Letra no válida. Las letras válidas son: ", letras_validas)
