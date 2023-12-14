"""
Marc Guerra Hernandez
14/12/2023
Examen pp2
"""

contador = 0

try:
    numero = int(input("Dame un numero: "))
    if numero > 0:
        for i in (str(numero)):
            contador += 1
        print("El numero", numero, "té", contador, "dígits")
    if numero < 0:
        print("no es un numero positivo.")

except ValueError:
    print("Eso no es un valor entero.")