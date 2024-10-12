class SalaModelo:
    salas_db = []  # Simula um banco de dados em memória para as salas

    def __init__(self, numero, capacidade, tipo):
        self.__numero = numero
        self.__capacidade = capacidade
        self.__tipo = tipo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    def adicionarSala(self):
        # Adiciona a sala à lista de salas, se ainda não estiver cadastrada
        for sala in SalaModelo.salas_db:
            if sala.numero == self.__numero:
                return f"Sala {self.__numero} já está cadastrada."

        SalaModelo.salas_db.append(self)
        return f"Sala {self.__numero} foi adicionada com sucesso!"

    def atualizarSala(self, numero=None, capacidade=None, tipo=None):
        # Atualiza os atributos da sala se valores não forem None
        if numero is not None:
            self.__numero = numero
        if capacidade is not None:
            self.__capacidade = capacidade
        if tipo is not None:
            self.__tipo = tipo
        return f"Sala {self.__numero} atualizada com sucesso!"

    def removerSala(self):
        # Remove a sala do sistema, caso esteja cadastrada
        for sala in SalaModelo.salas_db:
            if sala.numero == self.__numero:
                SalaModelo.salas_db.remove(sala)
                return f"Sala {self.__numero} foi removida com sucesso!"
        return f"Sala {self.__numero} não encontrada."
