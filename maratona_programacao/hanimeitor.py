import math
t = int(input()) #casos de teste

for contador in range(t):
    i, f = input().split(" ") #horario final e inicial hh:mm
    s, p = map(int, input().split(" ")) #tempo de atualização do relogio

    #convertendo para segundos
    hora_inicio, min_inicio = map(int, i.split(":"))
    segundos_inicio = hora_inicio*3600+min_inicio*60

    hora_fim, min_fim = map(int, f.split(":"))
    segundos_fim = hora_fim * 3600 + min_fim * 60

    duracao_em_milisseg = (segundos_fim-segundos_inicio)*1000

    s_milissegundos = s*1000

    mmc_s_p = (s_milissegundos*p)//math.gcd(s_milissegundos, p) #gcd eh mdc

    #quantas vezes o mmc cabe na duração
    if mmc_s_p == 0:
        print(0)
    else:
        print(duracao_em_milisseg // mmc_s_p) #numero de vezes que o relogio e o efeito piscaram ao msm tempo
