#contador que transforma em dicionario
from collections import Counter

n = int(input())

for i in range(n):
    texto = input().lower()

    conta_caracteres = {} #dicionario chave:valor, dic["chave1"] -> valor

    for chave in texto:
        if chave.isalpha(): #sabe se o caractere eh letra

            if chave in conta_caracteres:
                conta_caracteres[chave] += 1
            else:
                conta_caracteres[chave] = 1

    maior_freq =0
    for chave in conta_caracteres:
        if conta_caracteres[chave]>maior_freq: #se valor desse ai maior que o antig o maior, registra tam
            maior_freq=conta_caracteres[chave]

    letras_freq =[] #pega letras con essa freq
    for chave in conta_caracteres:
        if conta_caracteres[chave] == maior_freq:
            letras_freq.append(chave)

    letras_freq.sort()#ordem alfabetica

    print("".join(letras_freq))