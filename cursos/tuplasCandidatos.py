'''Construir um simulador de urna eletrônica. Inicialmente, o simulador deve permitir o
cadastro de candidatos. O usuário pode cadastrar quantos candidatos desejar. O cadastro
de um candidato envolve um número e seu nome. O número deve ser armazenado em
formato textual, mas deve possuir exatamente dois dígitos numéricos. A função isdigit() do
tipo textual pode ser usada para verificar se o texto é um número válido. Por fim, os
candidatos cadastrados devem ser mantidos em um dicionário (número: nome).

Após o cadastro de candidatos, o simulador deve iniciar a votação. O simulador
deve permitir uma quantidade indeterminada de votos. Para votar, o usuário deve informar
o número do candidato. O sistema deve mostrar o nome do candidato para o usuário
confirmar. Números inválidos devem ser computados como votos nulos. Já o texto vazio
deve ser contabilizado como voto em branco. A sumarização dos votos deve ser feita
usando um dicionário. Ao término da votação, o simulador deve mostrar o total e a
porcentagem de votos de cada candidato, nulos e brancos.'''
import os

dic_candidatos = {}
dic_votos = {}

def validaNumero(n):
    while not n.isdigit():
        print("Número inválido, digite novamente!!")
        n = input("\nDigite o número do candidato: ")

    else:
        while len(n) != 2:
            print("Número inválido, digite novamente! Só são aceitos números com 2 dígitos!")
            n = input("\nDigite o número do candidato: ")
        else:
            return n


def votacao():
    global total
    total = 0
    continuar = True

    while continuar:
        n_voto = input("Digite o número do candidato que vc deseja votar: ")

        if n_voto is None or n_voto=="" or n_voto==" ":
            dic_votos["Votos brancos"] +=1
            total += 1

        elif (not n_voto.isdigit()) or len(n_voto)!=2 or n_voto not in dic_candidatos :
            dic_votos["Votos nulos"] +=1
            total += 1

        else:
            print("\nO seu candidato é: ", dic_candidatos[n_voto].upper(),
                  "\nGostaria de confirmar a votação? Digite S para \"sim\" ou N para \"não\"")

            if input().upper() == "S":
                dic_votos[n_voto] += 1
                total += 1
                print("Votação confirmada!")
                os.system('cls')

            else:
                print("Voto cancelado!")

        sim_ou_nao = input("Deseja continuar? S para sim e N para não: ")
        if sim_ou_nao.upper() == "S":
            continuar = True
        else:
            continuar = False


try:
    qntd_candidatos = int(input("Digite a quantidade de candidatos que vc deseja cadastrar: "))

    for i in range(qntd_candidatos):
        numero_p_validar = input("\nDigite o número do candidato: ")
        numero = validaNumero(numero_p_validar)

        nome = input("Digite o nome do candidato: ")

        dic_candidatos[numero] = nome  # criação de um item em dicionário
        dic_votos[numero] = 0

    else:
        dic_votos["Votos brancos"] = 0
        dic_votos["Votos nulos"] = 0

        os.system('cls')  # limpa a 'tela'/console
        print("\n\nVOTAÇÃO VEEEI  :)\n")
        votacao()

        print("Os resultados da votação, com o total de", total, "votos, são:\n")

        for chave in dic_votos.keys():
            print(f"Para {chave}: {dic_votos[chave]} votos"
                  f"\nPorcentagem: {(dic_votos[chave]/total)*100}%;\n")
        else:
            print("FIM :)")

except ValueError:
    print("Ocorreu um erro de digitação de algum valor! Tente novamente.")
except Exception as e:
    print("Ocorreu o erro: ", e)