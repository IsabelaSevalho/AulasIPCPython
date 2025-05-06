vet =[]
for i in range(10):
    n = int(input())

    vet.insert(i, n)

x = int(input())
for item in vet:
    if item == x:
        print("Achei vei")
        break