class Main:
    

print("Testando Projeto")

from cliente import Cliente
from conta import Conta
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica


c1 = Cliente("Max", "12345-6789")
conta = Conta(c1.get_nome, 1222, 25)

conta.deposito(20)
conta.saque(50)
conta.extrato()




