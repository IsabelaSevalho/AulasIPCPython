impar =[]
par=[]

for i in range(15):
    n = int(input())

    if (n%2)==0: #par

        if len(par)<5:
            par.append(n)
        else:

            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par.clear()
            par.append(n)

    else:
        if len(impar) < 5:
            impar.append(n)
        else:

            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar.clear()
            impar.append(n)

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")

for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")