'''20.Construa um algoritmo que faça a conversão de um número que está na base decimal para
a base binária.

A conversão de números decimais em binários é realizada por meio da divisão sucessiva
do número decimal por 2, anotando-se o resto de cada divisão e invertendo a ordem deles
para obter a representação binária do número. Ao inverter a ordem dos restos, temos a
representação binária do número 10: 1010.'''

num = int(input("Digite um valor em base decimal: "))
aux = num
binario=""

while True:
    binario += str(aux%2)
    aux //=2

    if aux==0:
        binario = binario[::-1]
        break

print(f"O número {num} em formato binário é igual a: {binario}")