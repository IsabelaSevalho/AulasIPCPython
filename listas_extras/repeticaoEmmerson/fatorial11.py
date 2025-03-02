'''11.Fazer um algoritmo para achar o fatorial de um número N.'''
from math import factorial

n = int(input("Digite um número: "))
fat = 1

#onde começo, parar antes disso, diminuir 1 em n (meu contador)
for i in range(n, 0, -1):
    fat *= i
else:
    print(f"Fatorial sem função = {fat}")

fat = factorial(n)
print(f"Fatorial com função = {fat}")