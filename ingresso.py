#Ingresso
#Atributos: sessão, assento, preço, status (disponível, vendido).
#Métodos: emitirIngresso(), cancelarIngresso(), verificarDisponibilidade().

from sessao import Sessao
from sala import Sala
from filme import Filme


class Ingresso:

    ingressos_db = []

    def __init__(self, sessao: Sessao, assento: str, preco: float, status: str = "disponível"):
        self.__sessao = sessao
        self.__assento = assento
        self.__preco = preco
        self.__status = status

    @property
    def sessao(self) -> Sessao:
        return self.__sessao

    @sessao.setter
    def sessao(self, sessao: Sessao):
        self.__sessao = sessao
    
    @property
    def assento(self) -> str:
        return self.__assento

    @assento.setter
    def assento(self, assento: str):
        self.__assento = assento

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        if status in ["disponível", "vendido"]:
            self.__status = status
        else:
            raise ValueError("Status deve ser 'disponível' ou 'vendido'")

    def emitirIngresso(self):
        """Marca o ingresso como vendido, se disponível."""
        if self.__status == "disponível":
            self.__status = "vendido"
            Ingresso.ingressos_db.append(self)
            print(f"Ingresso para o assento {self.__assento} foi vendido.")
        else:
            print(f"Ingresso para o assento {self.__assento} já foi vendido.")

    def cancelarIngresso(self):
        """Cancela o ingresso, se vendido."""
        if self.__status == "vendido":
            self.__status = "disponível"
            Ingresso.ingressos_db.remove(self)
            print(f"Ingresso para o assento {self.__assento} foi cancelado e está disponível novamente.")
        else:
            print(f"Ingresso para o assento {self.__assento} não foi vendido, portanto não pode ser cancelado.")

    def verificarDisponibilidade(self):
        """Verifica se o ingresso está disponível."""
        return self.__status == "disponível"