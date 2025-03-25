'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.'''

def contaQuantas(numero, valor):
    cont = numero//valor
    return cont

n = int(input())
aux = n

cem = contaQuantas(aux, 100)
aux -= cem * 100

cinquenta=contaQuantas(aux, 50)
aux -= cinquenta * 50

vinte=contaQuantas(aux, 20)
aux -= vinte * 10

dez=contaQuantas(aux, 10)
aux -= dez * 10

cinco =contaQuantas(aux, 5)
aux -= cinco * 5

dois=contaQuantas(aux, 2)
aux -= dois * 2

um=contaQuantas(aux, 1)


print(f"{n}\n" +
      f"{cem} nota(s) de R$ 100,00\n"+
      f"{cinquenta} nota(s) de R$ 50,00\n"+
      f"{vinte} nota(s) de R$ 20,00\n"+
      f"{dez} nota(s) de R$ 10,00\n"+
      f"{cinco} nota(s) de R$ 5,00\n"+
      f"{dois}  nota(s) de R$ 2,00\n"+
      f"{um} nota(s) de R$ 1,00")