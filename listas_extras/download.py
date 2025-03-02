"""Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos)."""

tam_arquivo = float(input("Digite o tamanho do arquivo para dowload em MB: ")) #megabytes 1 = 8 megabits
velocidade = float(input("Digite a velocidade de um link de Internet em Mbps: ")) #megabits por seg
print(f"O tempo aproximado de dowload usando o link é: {round((((tam_arquivo)*8/velocidade)/60), 2)} minutos aproximadamente")