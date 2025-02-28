#15. Entrar com duas notas e imprimir a média final, truncada e arredondada.
from math import ceil

nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))

print(f"Para os valores {nota_1} e {nota_2} temos:\nMédia Final = {(nota_1+nota_2)/2}"
      f"\nMédia arredondada p baixo= {round((nota_1+nota_2)/2)}"
      f"\nMédia arredondada p cima= {ceil((nota_1+nota_2)/2)}")

#media truncada n sei \nMédia Truncada = {trunc((nota_1+nota_2)/2)}