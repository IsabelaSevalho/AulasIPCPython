import math
t = int(input())
for i in range(t):
    pa, pb, g1, g2 = input().split(" ")
    pa = int(pa)
    pb = int(pb)
    g1 = round(float(g1), 1)
    g2 = round(float(g2), 1)

    tempo_anos = 0

    while True:
        if pa <= pb and tempo_anos<=100:
            tempo_anos += 1
        else:
            break

        pa += math.floor(pa * (g1 / 100))
        pb += math.floor(pb * (g2 / 100))

    if tempo_anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{tempo_anos} anos.")