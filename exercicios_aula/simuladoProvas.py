ano = int(input())
if (ano%100)==0 and (ano%400)==0:
    print("Bissexto")
elif (ano%100)!=0 and (ano%4)==0:
    print("Bissexto")
else:
    print("nao")