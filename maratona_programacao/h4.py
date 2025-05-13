import math

T = int(input())  # número de casos de teste


def transforma_em_seg(horario):
    hora_inicio, min_inicio = map(int, horario.split(":"))
    return hora_inicio * 3600 + min_inicio * 60


for cont in range(T):
    i, t = input().split()  # horário inicial e final
    s, p = map(int, input().split())  # tempos de atualização

    # Converte para milissegundos
    duracao_em_milisseg = (transforma_em_seg(t) - transforma_em_seg(i)) * 1000
    s_ms = s * 1000

    mmc = (s_ms * p) // math.gcd(s_ms, p)

    if mmc == 0:
        print(0)
    else:
        print((duracao_em_milisseg // mmc) + 1)