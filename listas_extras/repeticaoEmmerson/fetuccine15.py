'''15.A série de Fetuccine difere da série de Ricci porque o termo de posição par é resultado da
subtração dos dois anteriores. Os termos ímpares continuam sendo o resultado da doma dos
dois elementos anteriores. Imprima os n primeiros termos da série de Fetuccine.'''

qntd_termos = int(input("Digite a quantidade de termos para a série Fetuccine: "))
termo_1 = int(input("Digite o primeiro termo da sua sequência: "))
termo_2 = int(input("Digite o segundo termo da sua sequência: "))

n = 0
anterior1 = termo_1
anterior2= termo_2

print("A sequência é: ")
print(termo_1)
print(termo_2)

for i in range(1, qntd_termos-1):

    if (i%2)==0:
        n = anterior2 - anterior1
        anterior1 = anterior2
        anterior2 = n
        print(n)

    else:
        n = anterior2 + anterior1
        anterior1 = anterior2
        anterior2 = n
        print(n)

