'''Leia um valor de ponto flutuante com duas casas decimais.
Este valor representa um valor monetário. A seguir, calcule o menor número de notas e
moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.'''

def quantasNotasParaValor(valor, numero):
    return valor//numero

def valorNovoCalculo(valor, qntd, numero):
    valor-= qntd *numero
    return valor

valor = float(input())
valor = round(valor, 2)
valor_novo = valor

cem = quantasNotasParaValor(valor_novo, 100)
valor_novo = valorNovoCalculo(valor_novo, cem, 100)

cinquenta = quantasNotasParaValor(valor_novo, 50)
valor_novo = valorNovoCalculo(valor_novo, cinquenta, 50)

vinte = quantasNotasParaValor(valor_novo, 20)
valor_novo = valorNovoCalculo(valor_novo, vinte, 20)

dez = quantasNotasParaValor(valor_novo, 10)
valor_novo = valorNovoCalculo(valor_novo, dez, 10)

cinco = quantasNotasParaValor(valor_novo, 5)
valor_novo = valorNovoCalculo(valor_novo, cinco, 5)

dois = quantasNotasParaValor(valor_novo, 2)
valor_novo = valorNovoCalculo(valor_novo, dois, 2)

um = quantasNotasParaValor(valor_novo, 1)
valor_novo = valorNovoCalculo(valor_novo, um, 1)

#0.05 e 0.01.
meio = quantasNotasParaValor(valor_novo, 0.5)
valor_novo = valorNovoCalculo(valor_novo, meio, 0.5)

quarto = quantasNotasParaValor(valor_novo, 0.25)
valor_novo = valorNovoCalculo(valor_novo, quarto, 0.25)

zerodez = quantasNotasParaValor(valor_novo, 0.10)
valor_novo = valorNovoCalculo(valor_novo, zerodez, 0.10)

zerocinco = quantasNotasParaValor(valor_novo, 0.05)
valor_novo = valorNovoCalculo(valor_novo, zerocinco, 0.05)

zeroum = quantasNotasParaValor(valor_novo, 0.01)
valor_novo = valorNovoCalculo(valor_novo, zeroum, 0.01)

print(f"NOTAS:\n" +
      f"{cem} nota(s) de R$ 100,00\n"+
      f"{cinquenta} nota(s) de R$ 50,00\n"+
      f"{vinte} nota(s) de R$ 20,00\n"+
      f"{dez} nota(s) de R$ 10,00\n"+
      f"{cinco} nota(s) de R$ 5,00\n"+
      f"{dois}  nota(s) de R$ 2,00\n"+
      f"MOEDAS:\n"+
      f"{um} moeda(s) de R$ 1.00\n"+
      f"{meio} moeda(s) de R$ 0.50\n"+
      f"{quarto} moeda(s) de R$ 0.25\n"+
      f"{zerodez} moeda(s) de R$ 0.10\n"+
      f"{zerocinco} moeda(s) de R$ 0.05\n"+
      f"{zeroum} moeda(s) de R$ 0.01")