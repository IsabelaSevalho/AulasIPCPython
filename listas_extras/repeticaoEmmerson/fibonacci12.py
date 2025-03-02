'''12.Fazer um programa para achar a série de Fibonacci dos n primeiros termos: 1 1 2 3 5 8 13 ...'''

qntd_termos = int(input("Digite a quantidade de termos que vc deseja ver na séria Fibonacci: "))
n=1
valor_anterior = 0
aux = n

#onde começo, parar antes disso
print(f"A série Fibonacci com {qntd_termos} é: ")
for i in range(0, qntd_termos):
    aux =n
    print(f"{n} ")
    n += valor_anterior
    valor_anterior = aux