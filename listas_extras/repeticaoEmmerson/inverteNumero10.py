'''10.Construa um algoritmo que leia um número inteiro N e imprima o mesmo na ordem inversa:
exemplo: dado 23457, a saída será 75432.'''

n = int(input("Digite um número inteiro: "))
n_str = str(n)
tam = len(n_str)
inv_n = ""

#onde começo, parar antes disso, diminuir 1 em n (meu contador)
for n in range(tam-1, -1, -1):
    inv_n += n_str[n]
else:
    print(int(inv_n))