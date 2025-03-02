'''15.A série de Fetuccine difere da série de Ricci porque o termo de posição par é resultado da
subtração dos dois anteriores. Os termos ímpares continuam sendo o resultado da doma dos
dois elementos anteriores. Imprima os n primeiros termos da série de Fetuccine.'''

qntd_termos = int(input("Digite a quantidade de termos para a série Fetuccine: "))
termo_1 = int(input("Digite o primeiro termo da sua sequência: "))
termo_2 = int(input("Digite o segundo termo da sua sequência: "))

n = termo_2
aux = n
termo_anterior = aux
print("A sequência é: ")
print(termo_1)

for i in range(1, qntd_termos):
    if (i%2)==0:
        print(n)
        aux = n
        n -= termo_anterior
        termo_anterior = aux
    else:
        print(n)
        aux = n
        n += termo_anterior
        termo_anterior = aux

#NÃO ESTOU CONSEGUINDO
