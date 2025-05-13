n, m = input().split(" ")
n = int(n)
m = int(m)

A = input().split(" ")
B = input().split(" ")
A = list(map(int, A)) #converte a lista p inteiro
B= list(map(int, B))

C=[]
for i in range(0, n):
    C.append(A[i])
for i in range(0, m):
    C.append(B[i])

lista_ordenada = sorted(list(set(C))) #ordena e tira repetida
valores = ""
for item in lista_ordenada:
    valores+= str(item) +" "

print(valores.strip())