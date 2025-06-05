Operacao = input()
M = []
Resultado = 0
quantidade =0
for i in range(12):
    vet = []
    for j in range(12):
        n = float(input())
        vet.append(n)
    M.append(vet)

# diagonal secundaria -> i+j = n(ordem)+1 (11) ->i+j == 13
# acima da ds: (i+j)<11

for i in range(12):
    for j in range(12):
        if j+i <11:
            Resultado += M[i][j]
            quantidade+=1

if Operacao == "S":
    print(f"{Resultado:.1f}")
else:
    print(f"{(Resultado/quantidade):.1f}")