vet1 =[]
vet2=[]

for i in range(10):
    n = int(input("Digite um número veyr:"))
    vet1.append(n)

for i in range(10):
    n = int(input("Digite dnv veyr:"))
    vet2.append(n)

s=[]
for i in range(10):
    s.append(vet1[i]+vet2[i])

print(s)