#Venda
#Atributos: cliente, ingressos, total, data, métodoDePagamento.
#Métodos: registrarVenda(), cancelarVenda(), gerarRecibo().

from cliente import Cliente
from filme import Filme
from sala import Sala
from sessao import Sessao
from ingresso import Ingresso
from datetime import datetime

class Venda:
    def __init__(self, cliente: Cliente, ingressos: list[Ingresso], metodo_de_pagamento: str):
        self.__cliente = cliente
        self.__ingressos = ingressos  # Agora é uma lista de ingressos
        self.__metodo_de_pagamento = metodo_de_pagamento
        self.__data = datetime.now()  # Registra a data e hora da venda
        self.__preco_total = self.calcular_preco_total()

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @property
    def ingressos(self) -> list[Ingresso]:
        return self.__ingressos

    @ingressos.setter
    def ingressos(self, ingressos: list[Ingresso]):
        self.__ingressos = ingressos
        self.__preco_total = self.calcular_preco_total()  # Atualiza o total quando os ingressos mudam

    @property
    def preco_total(self) -> float:
        return self.__preco_total

    @property
    def metodo_de_pagamento(self) -> str:
        return self.__metodo_de_pagamento

    @metodo_de_pagamento.setter
    def metodo_de_pagamento(self, metodo_de_pagamento: str):
        self.__metodo_de_pagamento = metodo_de_pagamento

    @property
    def data(self) -> datetime:
        return self.__data

    def calcular_preco_total(self) -> float:
        """Calcula o preço total somando o preço de todos os ingressos."""
        return sum(ingresso.preco for ingresso in self.__ingressos)

    def registrarVenda(self):
        """Registra a venda e marca os ingressos como vendidos."""
        for ingresso in self.__ingressos:
            if ingresso.verificarDisponibilidade():
                ingresso.emitirIngresso()
            else:
                print(f"Ingresso para o assento {ingresso.assento} já foi vendido.")
        print(f"Venda registrada para o cliente {self.__cliente.nome}. Total: R${self.__preco_total:.2f}")

    def cancelarVenda(self):
        """Cancela a venda e torna os ingressos disponíveis novamente."""
        for ingresso in self.__ingressos:
            if ingresso.status == "vendido":
                ingresso.cancelarIngresso()
        print(f"Venda cancelada para o cliente {self.__cliente.nome}. Ingressos disponíveis novamente.")

    def gerarRecibo(self) -> str:
        """Gera um recibo da venda com os detalhes."""
        recibo = f"Recibo de Venda\nCliente: {self.__cliente.nome}\nData: {self.__data.strftime('%d/%m/%Y %H:%M:%S')}\n"
        recibo += f"Método de Pagamento: {self.__metodo_de_pagamento}\nIngressos:\n"
        for ingresso in self.__ingressos:
            recibo += f"- Sessão: {ingresso.sessao.filme.titulo}, Assento: {ingresso.assento}, Preço: R${ingresso.preco:.2f}\n"
        recibo += f"Total: R${self.__preco_total:.2f}\n"
        return recibo


filme1 = Filme(titulo="O Poderoso Chefão", duracao="2h55min", genero="Drama", classificacao_etaria=18, sinopse="A saga da família Corleone.")
resultado = filme1.adicionarFilme()
print(resultado)
print(20*"=")

#Exemplo de Uso 2: Atualizar um Filme

filme1.atualizarFilme(titulo="O Poderoso Chefão - Parte I", duracao="3h", sinopse="Atualizada sinopse da saga da família Corleone.")
print(filme1)
print(20*"=")

#Exemplo de Uso 3: Registrar Venda de Ingressos

cliente1 = Cliente(nome="João Silva", fone="123456789", email="joao@example.com", historico_compras=None)
sessao1 = Sessao(filme=filme1, sala=Sala(1, 100, "3D"), data="20/10/2024", horario="19:00", ingressos_disponiveis=100)
ingresso1 = Ingresso(sessao=sessao1, assento="A1", preco=30.00)
ingresso2 = Ingresso(sessao=sessao1, assento="A2", preco=30.00)
venda = Venda(cliente=cliente1, ingressos=[ingresso1, ingresso2], metodo_de_pagamento="cartão de crédito")
venda.registrarVenda()
print(20*"=")

#Exemplo de Uso 4: Gerar Recibo de Venda

recibo = venda.gerarRecibo()
print(recibo)
print(20*"=")

#Exemplo de Uso 5: Adicionar Sala

sala1 = Sala(numero=1, capacidade=100, tipo="3D")
resultado = sala1.adicionarSala()
print(resultado)
print(20*"=")
#Exemplo de Uso 6: Remover Cliente

resultado_remover_cliente = cliente1.removerCliente()
print(resultado_remover_cliente)
print(20*"=")