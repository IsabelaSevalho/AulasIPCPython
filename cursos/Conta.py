class Conta:
    #pass

    def __init__(self, numero, nome_cliente):   #construtor
        self.numero = numero
        self.nome_cliente = nome_cliente
        self._protected_val = "protected"
        self.__private_val = "private"
        self.public_  = "public"

    def get_nomeCliente(self):
        return self.nome_cliente

    def set_nomeCliente(self, nome):
        self.nome_cliente = nome

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

contaaa = Conta(1, "MarianaContaDois")
print(contaaa.numero)
