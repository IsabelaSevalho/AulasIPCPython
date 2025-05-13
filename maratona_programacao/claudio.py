ab, c = map(int, input().split())

op = (ab + 180) % 360

if c == op:
    print("O Claudio ta do outro lado da roda!")
else:
    pr = (c - ab) % 360

    if 0 < pr < 180:
        print("Olha o Claudio ali em cima!")
    else:
        print("O Claudio ta ali embaixo!")