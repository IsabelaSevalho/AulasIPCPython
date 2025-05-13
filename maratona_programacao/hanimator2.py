import math

t = int(input())  # número de casos de teste

def transforma_em_seg(horario):
    hora_inicio, min_inicio = map(int, horario.split(":"))
    return hora_inicio * 3600 + min_inicio * 60

for contador in range(t):
    i, f = input().split()  # horário inicial e final no formato hh:mm
    s, p = map(int, input().split())  # tempos de atualização relogio em segundos e  animacao milissegundos

    #numero de vezes que o relogio e o efeito piscaram ao msm tempo?
    duracao_em_milisseg_competicao = (transforma_em_seg(f) - transforma_em_seg(i))*1000

    s_relogio_milissegundos = s*1000

    coincidencias = duracao_em_milisseg_competicao// (abs(s_relogio_milissegundos*p)//math.gcd(s_relogio_milissegundos, p))
    print(coincidencias)

