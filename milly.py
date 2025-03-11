'''5. Entrar com um número e imprimir se ele é positivo, negativo ou nulo.

a = int(input("Digite o valor: "))

if a>0:
    print("Positivo")
elif a<0:
    print("Negativo")
else:
    print("Nulo")
--------------------------------------------------------------------------------------'''

a = int(input("Digite um número: "))
b = int(input("Digite outro número:"))
maior = 0
menor = 0

if a<b:
    maior = b
    menor=a

else:
    maior = a
    menor = b

'''9.  sendo esta
diferença menor ou igual ao maior valor, multiplique o resultado por 2,5; caso
contrário divida o resultado pelo menor valor.'''

DIFERENCA = maior-menor

if DIFERENCA<= maior:
    DIFERENCA*=2.5
else:
    DIFERENCA/=menor

print(DIFERENCA)
