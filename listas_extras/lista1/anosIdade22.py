'''22. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual. Calcule e mostre:
a) A idade dessa pessoa.
b) Quantos anos essa pessoa terá em 2017.'''

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
print(f"Sua idade é {ano_atual-ano_nasc} e vc tinha {2017-ano_nasc} anos em 2017")