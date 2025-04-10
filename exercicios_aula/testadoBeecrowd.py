n = int(input())
posicao_inicial = input()
final = posicao_inicial

for i in range(n):
    movimento = int(input())

    if movimento == 1:
        if final == "A":
            final = "B"
        elif final == "B":
            final = "A"

    elif movimento == 2:
        if final == "B":
            final = "C"
        elif final == "C":
            final = "B"

    else:
        if final == "A":
            final = "C"
        elif final == "C":
            final = "A"

print(final)
