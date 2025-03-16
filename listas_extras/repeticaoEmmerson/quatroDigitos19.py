'''19.O número 3025 possui a seguinte característica:
30 + 25 = 55
55 elevado a 2 = 3025
Fazer um algoritmo que pesquise e imprima todos os números de quatro dígitos que
apresentam tal característica.'''

for i in range(1000, 9999):
    val1= int(str(i)[0]+str(i)[1])
    val2= int(str(i)[2]+str(i)[3])

    if i == (val1+val2)**2:
        print(i)