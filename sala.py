#Sala
#Atributos: número, capacidade, tipo (2D, 3D, IMAX).
#Métodos: adicionarSala(), atualizarSala(), removerSala().


class Sala:

    salas_db = []

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
        # Adiciona o sala ao "banco de dados"
        Sala.salas_db.append(self)
        return f"Sala '{self.__numero}' adicionada com sucesso."

    def atualizarSala(self, numero=None, capacidade=None, tipo=None):
        # Atualiza os atributos do filme se os novos valores forem fornecidos
        if numero is not None:
            self.__numero = numero
        if capacidade is not None:
            self.__capacidade = capacidade
        if tipo is not None:
            self.__tipo = tipo
        return f"Sala atualizada: {self.__numero}, {self.__capacidade}, {self.__tipo}"

    def removerSala(self):
        # Remove o filme do "banco de dados"
        if self in Sala.salas_db:
            Sala.salas_db.remove(self)
            return f"Sala '{self.__numero}' removida com sucesso."
        else:
            return f"Sala '{self.__numero}' não encontrada."

    def __str__(self):
        return (f"Sala: {self.__numero}\n"
                f"Capacidade: {self.__capacidade}\n"
                f"Tipo: {self.__tipo}\n")