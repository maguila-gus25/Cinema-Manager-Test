from salamodelo import SalaModelo


class SalaControlador:
    def __init__(self):
        pass

    def adicionar_sala(self, numero, capacidade, tipo):
        # Cria uma nova sala e tenta adicioná-la ao "banco de dados"
        sala = SalaModelo(numero, capacidade, tipo)
        return sala.adicionarSala()

    def atualizar_sala(self, numero, capacidade=None, tipo=None):
        # Procura a sala pelo número e, se encontrada, atualiza os atributos
        for sala in SalaModelo.salas_db:
            if sala.numero == numero:
                return sala.atualizarSala(numero=numero, capacidade=capacidade, tipo=tipo)
        return f"Sala {numero} não encontrada para atualização."

    def remover_sala(self, numero):
        # Procura a sala pelo número e, se encontrada, remove-a
        for sala in SalaModelo.salas_db:
            if sala.numero == numero:
                return sala.removerSala()
        return f"Sala {numero} não encontrada para remoção."

    def listar_salas(self):
        # Lista todas as salas cadastradas no sistema
        if not SalaModelo.salas_db:
            return "Nenhuma sala cadastrada."
        return [f"Número: {salamodelo.numero}, Capacidade: {salamodelo.capacidade}, Tipo: {salamodelo.tipo}" for salamodelo in SalaModelo.salas_db]
