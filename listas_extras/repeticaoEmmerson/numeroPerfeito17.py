'''17.Fazer um algoritmo para verificar se um número lido é número perfeito. Número perfeito é
aquele que é igual a soma dos seus divisores. Por exemplo: 6 = 1 + 2 + 3'''

n = int(input("Digite um número: "))
soma_divisores = 0

for i in range(1, n):
    if n%i==0:
        soma_divisores+=i

if n==soma_divisores:
    print(f"{n} É perfeito!")
else:
    print(f"{n} NAO é perfeito!")