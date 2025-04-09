T = int(input())

for i in range(T):
    n = int(input())
    nomes = input().split(" ")
    presencas = input().split(" ")
    nao_cumpriram = ""

    for i_aluno in range(n):
        cont_presencas = 0
        cont_aulas = 0
        presencas_aluno = presencas[i_aluno]

        for i_frequencia in range(len(presencas_aluno)):
            if presencas_aluno[i_frequencia] == "A":
                cont_aulas += 1
            elif presencas_aluno[i_frequencia] == "P":
                cont_presencas += 1
                cont_aulas += 1
            else:
                continue

        if cont_presencas < (0.75 * cont_aulas):
            nao_cumpriram += nomes[i_aluno]+" "

    print(nao_cumpriram.strip())