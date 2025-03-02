"""16. Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão
para o garçom. Crie um algoritmo em PORTUGOL que leia o valor gasto com despesas
realizadas em um restaurante e imprima o valor da gorjeta e o valor total com a gorjeta."""

despesas = float(input("Digite o valor das despesas: "))
gorjeta = despesas * 0.1
total = despesas * 1.1 #adiciona 10%
print("Gorjeta: "+str(gorjeta)+"\nTotal: "+str(total))