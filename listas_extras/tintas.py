'''Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total.'''
import math

area_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
# 1/l --- 3/m
litros_necessarios= area_pintada/3
qntd_latas = math.ceil(litros_necessarios/18) #math.ceil arredonda para cima
preco_total= qntd_latas*80

print("A quantidade de latas que devem ser usadas são: ", qntd_latas, "\nJá o preço total é: R$", preco_total)