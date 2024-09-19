#Cliente
#Atributos: nome, email, telefone, históricoDeCompras.
#Métodos: cadastrarCliente(), atualizarCliente(), removerCliente().

class Cliente:

    clientes_db = []

    def __init__(self, nome: str, fone: str, email: str, historico_compras: None):
        self.__nome = nome
        self.__fone = fone
        self.__email = email
        self.__historico_compras = historico_compras

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        self.__fone = fone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    def cadastrarCliente(self):
        #Cadastra o cliente
        Cliente.clientes_db.append(self)
        return f"Cliente: '{self.__nome}' adicionado com sucesso."

    def atualizarCliente(self, nome=None, fone=None, email=None, historico_compras=None):
        # Atualiza os atributos do cliente se os novos valores forem fornecidos
        if nome is not None:
            self.__nome = nome
        if fone is not None:
            self.__fone = fone
        if email is not None:
            self.__email = email
        if historico_compras is not None:
            self.__historico_compras
        return f"Cliente atualizado: {self.__nome}, {self.__fone}, {self.__email}, {self.__historico_compras}"

    def removerCliente(self):
        # Remove o cliente do "banco de dados"
        if self in Cliente.clientes_db:
            Cliente.clientes_db.remove(self)
            return f"Cliente '{self.__nome}' removido com sucesso."
        else:
            return f"Cliente '{self.__nome}' não encontrado."

    def __str__(self):
        return (f"Nome: {self.__nome}\n"
                f"Fone: {self.__fone}\n"
                f"Email: {self.__email}\n"
                f"Histórico de Compras: {self.__historico_compras}\n")