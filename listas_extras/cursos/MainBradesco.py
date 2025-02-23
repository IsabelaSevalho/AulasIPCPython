class MainBradesco:
    pass

print("Olá, a classe MainBradesco está funcionando!!")

from listas_extras.cursos.Cliente import Cliente
cliente1 = Cliente("Mariana", 98888)

print (cliente1)
print(cliente1.nome, cliente1.cpf)