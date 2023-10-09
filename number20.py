a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for b in range(10):
    num = float(input("Digite um número: "))
    a[b] += num

for c in range(10):
    if a[c] % 2 != 0:
        print(a[c], "é ímpar")

for c in range(10):
    if a[c] % 2 == 0:
        print(a[c], "é par")

for c in range(10):
    if a[c] >= 0:
        print(a[c], "é positivo")

for c in range(10):
    if a[c] < 0:
        print(a[c], "é negativo")

for c in range(10):
    if a[c] == 0:
        print(a[c])