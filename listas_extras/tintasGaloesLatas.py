'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
 que custam R80,00 ou em galõesde 3,6 litros,que custam R 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os
 respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''
import math

area_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
qntd_tinta = area_pintada/6
qntd_tinta_folga = qntd_tinta + ((10/100)*qntd_tinta)
#1l -- 6m

qntd_latas = math.ceil(qntd_tinta_folga/18)
preco_so_latas = qntd_latas*80
print("Comprando apenas latas de 18 litros temos a quantidade de ", qntd_latas, " latas por R$", preco_so_latas)

qntd_galoes = math.ceil(qntd_tinta_folga/3.6)
preco_so_galoes = qntd_galoes*25
print("Comprando apenas galões de 3,6 litros temos a quantidade de ", qntd_galoes, " galões por R$", preco_so_galoes)

qntd_latas_mistura = qntd_tinta_folga//18
qntd_litros_latas = qntd_latas_mistura *18

resto_tinta = qntd_tinta_folga-qntd_litros_latas

qntd_galoes_mistura = math.ceil(resto_tinta/3.6)
preco_mistura = qntd_galoes_mistura*25 + qntd_latas_mistura*80
print("Ao misturar latas e galões, de forma que o desperdício de tinta seja menor temos a quantidade de ",
      qntd_latas_mistura, "latas e ", qntd_galoes_mistura,"galões por R$", preco_mistura)
