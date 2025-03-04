'''Desenvolver um algoritmo que construa uma lista de tuplas com nome e salário de
funcionários. Em seguida, o código deve recalcular os salários considerando os seguintes
aumentos:
• 20% para salários de até R$2.000,00;
• 15% para salários entre R$2.000,00 e R$5.000,00;
• 5% para salários maiores que R$5.000,00;

Por fim, o código deve exibir o total de aumento (total dos salários novos menos o total de
salários antigos e os nomes dos funcionários com salários menores que R$2.000,00.'''
lista_tuplas = []

try:
    qntd_func = int(input("Digite a quantidade de funcionários que vão participar do cálculo de salários: "))

    for i in range(qntd_func):
        nome = input("Digite o nome do funcionário: ")
        salario = float(input("Digite o valor do seu salário: "))
        func = (nome, salario)
        lista_tuplas.append(func)

except:
    print("Ocorreu algum erro!")

else:
    lista_reajuste = []

    for item in lista_tuplas:
        nome , salario = item

        if salario<=2000.00:
            salario += 0.2*salario
        elif salario>2000.00 and salario<=5000.00:
            salario += 0.15 * salario
        else:
            salario += 0.05 * salario

        func = (nome, salario)
        lista_reajuste.append(func)
    else:
        print("Considerando as porcentagens, os novos salários são:")
        for item in lista_reajuste:
            print(item)


