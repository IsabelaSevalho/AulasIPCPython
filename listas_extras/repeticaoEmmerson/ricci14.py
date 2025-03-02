'''14.A série de Ricci difere da série de Fibonacci porque os dois primeiros termos podem ser
definidos pelo usuário. Imprima os n primeiros termos da série de Ricci.'''

qntd_termos = int(input("Digite a quantidade de termos para a série Ricci: "))
termo_1 = int(input("Digite o primeiro termo da sua sequência: "))
termo_2 = int(input("Digite o segundo termo da sua sequência: "))

n = termo_1
aux = termo_1
diferenca_sequencia = termo_2-termo_1

for i in range(0, qntd_termos):
    print(n)
    aux =n
    n+=diferenca_sequencia
    diferenca_sequencia = aux