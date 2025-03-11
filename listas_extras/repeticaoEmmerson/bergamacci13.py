'''13.Fazer um programa para achar a série de Bergamacci dos n primeiros termos: 1 1 1 1 3 5 9 17 ...'''

qntd_termos = int(input("Digite a quantidade de termos que vc deseja ver na séria Bergamacci: "))
n= 1
val_1 = 0
val_2 = 0
val_3 = 0

print(f"A sequência Bergamacci com {qntd_termos} termos é:")
for i in range(qntd_termos):

    if i<4:
        val_1 = 1
        val_2 = 1
        val_3 = 1
        n=1
    else:
        val_1 = val_2
        val_2 = val_3
        val_3 = n
        n = val_1 + val_2 + val_3

    print(n)

#funcionando com gambiarra