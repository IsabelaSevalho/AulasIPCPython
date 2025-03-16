'''2. Ler 10 valores e escrever quantos destes valores são positivos.'''

cont = 0
positivos = 0

while cont<10:
    val = int(input())
    if val>0:
        positivos+=1
    cont+=1
print(f"{positivos} numeros sao positivos")

