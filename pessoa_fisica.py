class PessoaFisica(Cliente):
    def __init__(self, nome, telefone, cpf):
        super().__init__(nome, telefone)
        self._cpf = cpf

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def __str__(self):
        return (f"Pessoa Física: {self.get_nome()},"
                f" Telefone: {self._telefone},"
                f" CPF: {self._cpf}")
