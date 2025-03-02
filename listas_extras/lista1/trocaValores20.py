'''20. Elabore um algoritmo que troque 3 variáveis, a, b, e c, de forma que a fique com o valor de b, b com o
valor de c e c com o valor de a, supondo que, inicialmente, a=5, b=10 e c=8.'''
a=5
b=10
c=8

extra = a
a = b
b = c
c = extra
print(f"Valores após troca: \na = {a}\nb = {b}\nc = {c}")