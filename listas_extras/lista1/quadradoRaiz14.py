"""14. Entrar com um número e imprimir a seguinte saída: numero, o quadrado do número e a raiz
quadrada desse número."""
from math import sqrt

n = int(input("Digite um número: "))
print(f"Para o número {n}, seu quadrado e sua raiz quadrada são, respectivamente, {n**2} e {sqrt(n)}")