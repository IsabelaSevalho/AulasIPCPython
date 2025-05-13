n = int(input())

if n==1:
    print(1)
elif n==3 or n==2:
    print("NO SOLUTION")
else:
    #nenhum número esteja imediatamente ao lado de outro cuja diferença seja exatamente 1
    permutacao = []

    for i in range(2, n+1, 2): #par
        permutacao.append(str(i))

    for i in range(1, n+1, 2): #impar
        permutacao.append(str(i))


    print(" ".join(permutacao))