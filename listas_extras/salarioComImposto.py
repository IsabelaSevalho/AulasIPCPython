'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

Salário Bruto : R −IR(11
INSS (8%) : R −Sindicato(5  = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

ganho_por_hora = float(input("Informe quanto vc ganha por hora: "))
n_hrs_trabalhadas = int(input("Informe o número de horas trabalhadas no mês: "))
salarioBruto = ganho_por_hora*n_hrs_trabalhadas
valorINSS = (8/100)*salarioBruto
valorSindicato = (5/100)*salarioBruto
imposto= (11/100)*salarioBruto
salarioLiquido = salarioBruto-(valorINSS+valorSindicato+imposto)
print("Salário bruto: R$", salarioBruto,
      "\nValor INSS: R$", valorINSS,
      "\nValor sindicato: R$", valorSindicato,
      "\nSalário líquido: R$", salarioLiquido)