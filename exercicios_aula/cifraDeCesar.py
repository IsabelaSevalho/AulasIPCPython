n = int(input())
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]  # 0 a 25

for i in range(n):
    palavra_codificada = input()
    qnts_posicoes = int(input())  # quantas moveu para direita

    txt_decodificado = ""

    for item in palavra_codificada:
        posicao_letra = alfabeto.index(item)

        posicao_nova_letra = (posicao_letra - qnts_posicoes) % 26
        txt_decodificado += alfabeto[posicao_nova_letra]

    print(txt_decodificado)