'''• A calculadora consiste em um console onde o usuário digita comandos;
• O usuário pode digitar expressões aritméticas para serem calculadas, ver o histórico
de expressões ou sair;
• Os comandos h e s são usados respectivamente para histórico e sair;
• Deve ser realizado tratamento de exceção no cálculo da expressão digitada para
garantir que a mesma não possuir erros;
• O histórico deve guardar apenas as expressões sem erros.'''

historico=[]

def calcula(expressao):
    try:
        return eval(expressao) #executa a string como se fosse um cod python
    except:
        print('Expressão inválida!!')
        return None

def exibeHistorico():
    if len(historico) == 0:
        print("Você não possui nada registrado no seu histórico!\n")
    else:
        print("Seu histórico:")
        for item in historico:
            print(item)
        else:
            print("Fim do histórico!")

def adicionaAoHistorico(expressao, resultado):
    historico.append(f"{expressao} = {resultado}")

print("Calculadora :)")
while True:
    exp = input("\nDigite uma expressão matemática\nCaso não queira mais calcular, digite \'s\' para sair OU \'h\' para acessar seu histórico: ")
    if exp.lower() == 's':
        print("Finalizando a calculadora!")
        break
    elif exp.lower() == 'h':
        exibeHistorico()
    else:
        resultado = calcula(exp)
        if resultado is not None:
            adicionaAoHistorico(exp, resultado)
            print("O resultado da operação digitada é", resultado)

