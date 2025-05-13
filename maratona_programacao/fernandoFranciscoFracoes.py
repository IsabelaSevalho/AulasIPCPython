from fractions import Fraction
n = int(input())
itens = input().split()

numeros = []
operadores = []

for item in itens:
    if item in '+-*/':
        operadores.append(item)
    else:
        if '/' in item:
            num, den = item.split('/')
            numeros.append(Fraction(int(num), int(den)))
        else:
            numeros.append(Fraction(int(item), 1))

resultado = numeros[0]
for i in range(len(operadores)):
    operador = operadores[i]
    proximo_numero = numeros[i + 1]

    if operador == '+':
        resultado += proximo_numero
    elif operador == '-':
        resultado -= proximo_numero
    elif operador == '*':
        resultado *= proximo_numero
    elif operador == '/':
        resultado /= proximo_numero

print(f"{resultado.numerator}/{resultado.denominator}")