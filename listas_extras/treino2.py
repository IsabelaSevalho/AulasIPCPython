'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''
def dobroArea():
    lado=float(input("Digite o valor do lado do quadrado: "))
    print("Área é: ", lado*lado, "\nDobro da área é: ", (lado*lado)*2)

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''
def salario():
    ganho_por_hora = float(input("Informe quanto vc ganha por hora: "))
    n_hrs_trabalhadas = int(input("Informe o número de horas trabalhadas: "))
    print("Seu salário no mês referido é: ", ganho_por_hora*n_hrs_trabalhadas)

'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).'''
def FParaC():
    f= float(input("Digite um valor em Fahrenheit: "))
    print("Esse valor em Celsius é igual a: ", 5 * ((f-32) / 9))

'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''
def CparaF():
    c = float(input("Digite um valor em Celsius: "))
    print("Esse valor em Fahrenheit é igual a: ", (9*c + 160)/5)

'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''
def multiplicacoes():
    num_int_1 = int(input("Digite um número inteiro: "))
    num_int_2 = int(input("Digite outro número inteiro: "))
    num_float = float(input("Digite um número decimal: "))
    print("Produto do dobro do primeiro com metade do segundo: ", (num_int_1*2)*(num_int_2/2),
          "\nSoma do triplo do primeiro com o terceiro: ", (num_int_1*3)+ num_float,
          "\nTerceiro elevado ao cubo: ", num_float**3)

'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58'''
def pesoIdeal():
    altura= float(input("Digite sua altura: "))
    print("Seu peso ideal é: ", (72.7*altura) - 58)

'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''
def pesoIdealHM():
    altura= float(input("Digite sua altura: "))
    sexo= bool(input("Digite \'True\' para sexo feminino e \'False\' para sexo masculino: "))

    if sexo==True:
        print("Seu peso ideal é: ", (62.1*altura) - 44.7) #fem
    else:
        print("Seu peso ideal é: ", (72.7*altura) - 58)  # masc

dobroArea()
salario()
FParaC()
CparaF()
multiplicacoes()
pesoIdeal()
pesoIdealHM()