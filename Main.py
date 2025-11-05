class Main:
    

print("Testando Projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Max", "12345-6789")
conta = Conta(c1.get_nome, 1222, 25)

conta.deposito(20)
conta.saque(50)
conta.extrato()




