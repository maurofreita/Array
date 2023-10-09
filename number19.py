A = []

contador = 0

numeros = 0

while contador < 9:
    if numeros % 2 == 0:
        numeros += 1
        A.append(numeros)
    else:
        numeros += 2
        A.append(numeros)
        contador += 1
print(A)