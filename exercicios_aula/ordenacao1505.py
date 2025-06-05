TAM = int(input("Tamanho da lista: "))
a=[]
for i in range(TAM):
    a.append(int(input(f"Valor {i+1}: ")))

print(a)

for vezes in range(TAM-1):
    trocou = False
    for i in range(TAM-1, vezes, -1):
        if a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            trocou = True
    if not trocou:
        break

print(a)