"""
Marc Guerra Hernandez
14/12/2023
Examen pp2
"""

numletra = 0

letra = input("Dame una letra: ")
frase = input("Dame una frase: ")

for i in frase:
    if i == letra:
        numletra += 1

print(numletra)
