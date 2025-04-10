'''L = int(input())
C = int(input())
inferior_direito=0

for i in range(1, L+1):
    for j in range(1, C+1):
        if ((i%2)!=0 and (j%2)!=0) or (i==j) or ((j-i)!=3):
            inferior_direito= 1
        else:
           inferior_direito= 0

print(inferior_direito) FORMA QUE DEU ERRADO
'''

'''L = int(input())
C = int(input())
inferior_direito = 1
par = 0
impar = 1

for i in range(1, L + 1):

    if inferior_direito == 1:  # ultimo for branco
        impar = 0
        par = 1
    else:  # ultimo for preto
        impar = 1
        par = 0

    for j in range(1, C + 1):

        if (j % 2) == 0:  # par
            inferior_direito = par
        else:
            inferior_direito = impar

print(inferior_direito)'''

L = int(input())
C = int(input())
inferior_direito = 1

if (L % 2) != 0:
    inferior_direito = 1  # comeca branco se linha impar
else:
    inferior_direito = 0  # comeca preto se linha par

# se for coluna impar, termina igual comecou. Par muda
if (C % 2) == 0:
    if inferior_direito == 1:
        inferior_direito = 0
    else:
        inferior_direito = 1

print(inferior_direito)