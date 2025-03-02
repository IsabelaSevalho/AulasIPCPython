#tipos de variáveis
a = 5
b = 9.5
c = True
d = "Jhon" #var globais

def tiposVar():
    print("Tipo da variável a: ", type(a),
          "\nTipo da variável b: ", type(b),
          "\nTipo da variável c: ", type(c),
          "\nTipo da variável d: ", type(d))


#conversão da entrada de dados
def conversaoEntrada():
    booleano_verdadeiro = bool(input("Digite True ou False: "))
    booleano_fake = input("Digite True ou False: ")

    print("Tipo da variável booleano_verdadeiro: ", type(booleano_verdadeiro),
          "\nTipo da variável booleano_fake: ", type(booleano_fake))

#usos do print
def usosPrint():
    print(f"Usando o format é assim para exibir a varíavel {a} que vc quiser")  # format
    print("Apenas colocando no print fora das aspas e lembrando de separar por vírgula: ",a, "gtfrdctrd")  # assim suporta tipos diferentes
    print("Convertendo para string a variável " + str(a) + " já que é possível")  # concatenação = unir duas ou mais strings em uma única string

def concatena():
    x = "Python "
    y = "is "
    z = "awesome"
    print(x + y + z)

    txt = f"The price is {20 * 59} dollars"
    print(txt)


#var globais != var funcoes
x = "awesome"

def globaisCompara():
    x = "fantastic"
    print("Python is " + x)

#globaisCompara()
#print("Python is " + x)

#Se você usar a global palavra-chave, a variável pertence ao escopo global
def usoDeGlobal():
    global e
    e = "fantastic"

usoDeGlobal()
print("Python is " + e)




