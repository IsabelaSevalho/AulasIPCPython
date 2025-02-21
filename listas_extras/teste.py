#outras func
def continuarOuNao(exibicao, numeroFuncao):
  #condição para ver se continua a executar ou nao
  resposta = input("Digite \"S\" para parar na exibição do resultado da última operação ou \"N\" para continuar: ")
  if resposta == "Sim":
    print(exibicao)
  else:
    print(exibicao)
    if numeroFuncao == 1:
      funcaoSoma()
    elif numeroFuncao == 2:
      mediaNotas()
    elif numeroFuncao ==3:
      converteMetrosCm()
    elif numeroFuncao == 4:
      areaCirculo()
    else:
      return 0

def verificaNotasValidas(notas):
  for item in notas:
    if item<0 or item>10:
      return False
    else:
      return True

#func 1
def funcaoSoma():
  soma1 = int(input("Escolha um número para ser somado: "))
  soma2 = int(input("Escolha outro número para ser somado: "))
  continuarOuNao(("O valor da soma é: ", (soma1+soma2)), 2)

#func 2
def mediaNotas():
  notas =[]
  nota1 = float(input("Digite a nota 1: "))
  notas.append(nota1)

  nota2 = float(input("Digite a nota 2: "))
  notas.append(nota2)

  nota3 = float(input("Digite a nota 3: "))
  notas.append(nota3)

  nota4 = float(input("Digite a nota 4: "))
  notas.append(nota4)

  if verificaNotasValidas(notas) == True:
    continuarOuNao(("O valor da média é: ", ((nota1 + nota2 + nota3 +nota4)/4)), 3)
  else:
    print("Notas inválidas!!")
    mediaNotas()

#func 3
def converteMetrosCm():
  metros = float(input("Digite um valor em metros: "))
  continuarOuNao((metros ," em cm é equivalete a: ", metros*100), 4)

#func 4
def areaCirculo():
  raio = int(input("Digite o raio do círculo q vc deseja saber a área: "))
  continuarOuNao(("A área é: ", (2*3.14*raio)), 0)


print("Alo mundo")
numeroAExibir = int(input("Digite um número para ser exibido: "))
continuarOuNao(("Número da exibição: " , numeroAExibir), 1)
