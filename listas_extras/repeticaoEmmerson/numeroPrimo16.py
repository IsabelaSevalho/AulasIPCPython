'''16.Fazer um algoritmo para verificar se um número lido é primo ou não. Número primo é aquele
que é divisível por 1 e por ele mesmo.'''

n = int(input("Digite um número: "))
contValidos = 0
contInvalidos = 0

for i in range(1, n+1):
    if n%i==0 and i!=1 and i!=n:
        contInvalidos+=1

else:
    if contInvalidos!=0:
        print(f"O número {n} NÃO é primo!")
    else:
        print(f"O número {n} é primo!")


