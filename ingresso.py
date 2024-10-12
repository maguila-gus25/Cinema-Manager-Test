#Ingresso
#Atributos: sessão, assento, preço, status (disponível, vendido).
#Métodos: emitirIngresso(), cancelarIngresso(), verificarDisponibilidade().

from sessao import Sessao
from sala import Sala
from filme import Filme


class Ingresso:

    ingressos_db = []

    def __init__(self, sessao: Sessao, assento: str, preco: float):
        self.__sessao = sessao
        self.__assento = assento
        self.__preco = preco

    @property
    def sessao(self) -> Sessao:
        return self.__sessao

    @sessao.setter
    def sessao(self, sessao: Sessao):
        self.__sessao = sessao

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco


    def emitirIngresso(self):
        """Marca o ingresso como vendido, se disponível."""
        if sessao.__ingressos_diponiveis > 0:
            Ingresso.ingressos_db.append(self)
            sessao.__ingresso_diponiveis -= 1
            print(f"Ingresso para o filme {self.__sessao.__filme} foi vendido.")
        else:
            print(f"Ingresso para o assento {self.__assento} já foi vendido.")

    def cancelarIngresso(self):
        """Cancela o ingresso, se vendido."""
        self.__sessao.__ingressos_disponiveis += 1
        self.ingressos_db.remove(self)
        print(f"Ingresso para o filme {self.__sessao.__filme} foi cancelado e está disponível novamente.")
        

    def verificarDisponibilidade(self):
        """Verifica se o ingresso está disponível."""
        return self.__sessao.__ingressos_disponiveis > 0
