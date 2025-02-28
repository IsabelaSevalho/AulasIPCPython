"""Entrar com os valores dos catetos de um triângulo retângulo e imprimir a hipotenusa.
Hipotenusa é igual a raiz quadrada do cateto oposto ao quadrado somado ao cateto adjacente
ao quadrado."""
import math #biblioteca para calcular sen cos e tg

def hipotesusa():
    adj = float(input("Digite o valor do cateto adjacente: "))
    op = float(input("Digite o valor do cateto oposto: "))
    hipotenusa= (adj**2 + op**2)**(1/2) #+ dos quadrados dos catetos é igual a hipotesusa**2, transformando raiz em numero cm expoente
    print(f"O valor da hipotenusa é: {hipotenusa}")
    #cosSenTan(adj, op, hipotenusa)

'''Entrar com um ângulo em graus e imprimir: seno, co-seno e tangente desse ângulo.'''
def cosSenTan(adj, op, hip):
    if adj is None and op is None and hip is None:
        ang = float(input("Digite o valor do ângulo em graus: "))

        #cálculo exige valor em radianos, pois
        rad = math.radians(ang)
        sen = math.sin(rad)
        cos = math.cos(rad)
        tg = math.tan(rad)

        print(f"Seno: {sen}\nCosseno: {cos}\nTangente: {tg}")
        print(f"Seno: {round(sen, 2)}\nCosseno: {round(cos, 2)}\nTangente: {round(tg, 2)}") #arrdondando para 2 casas dec


    elif adj is None and op is not None and hip is not None:
        print(f"Seno: {op/hip}")

    elif adj is not None and op is None and hip is not None:
        print(f"Cosseno: {adj/hip}")

    elif adj is not None and op is not None and hip is None:
        print(f"Tangente: {op/adj}")

    else:
        print(f"Seno: {op/hip}\nCosseno: {adj/hip}\nTangente: {op/adj}")

hipotesusa()
#cosSenTan(None, None, None)
#cosSenTan(None, 3, 4)
#cosSenTan(4, None, 4)
#cosSenTan(6, 3, None)