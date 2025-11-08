class PessoaJuridica(Cliente):
    def __init__(self, nome, telefone, cnpj):
        super().__init__(nome, telefone)
        self._cnpj = cnpj

    def get_cnpj(self):
        return self._cnpj

    def set_cnpj(self, cnpj):
        self._cnpj = cnpj

    def __str__(self):
        return (f"Pessoa Jurídica: {self.get_nome()}"
                f", Telefone: {self._telefone}"
                f", CNPJ: {self._cnpj}")