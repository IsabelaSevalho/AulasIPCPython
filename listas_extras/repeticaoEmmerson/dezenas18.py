'''18.Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas pelos seus
dois primeiro e dois últimos dígitos. Exemplo: 1456 : 14 e 56.
Construa um algoritmo que imprima todos os números de quatro algarismos cuja raiz quadrada seja a soma das dezenas
formadas pela divisão acima. Exemplo: raiz de 9801 = 99 = 98 + 01.'''
import math

for i in range(1000, 9999):
    val1= int(str(i)[0]+str(i)[1])
    val2=int(str(i)[2]+str(i)[3])
    if math.sqrt(i)==val1+val2:
        print(i)