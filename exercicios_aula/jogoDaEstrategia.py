j, r = input().split()
j = int(j)
r= int(r)
valores = input().split()

maior_pontuacao = 0
numero_maior = 0

for jogador in range(j):
    pontuacao = 0
    for rodada in range(r):
        indice = rodada * j + jogador
        pontuacao += int(valores[indice])

    if pontuacao >= maior_pontuacao:
        maior_pontuacao = pontuacao
        numero_maior = jogador + 1

print(numero_maior)