'''for i in range(10):
    n = int(input("Digite um número: "))

    if (n % 2) == 0:
        print(f"{n} é um número par")
    else:
        print(f"{n} é um número ímpar")'''

'''n = int(input())
fat =1

for i in range(n, 0, -1): #start, stop (do start até antes do stop), step (passo)
    fat*=i

print(f"Fatorial de {n} eh: {fat}")'''

maior =0

for i in range(10):
    n = int(input("Digite um numero: "))

    if(i==0):
        maior = n
    else:
        if n > maior:
            maior = n
        else:
            continue

print(f"O maior número eh: {maior}")

