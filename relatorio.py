class Relatorio:

    @staticmethod
    def filmesMaisAssistidos():
        # Cria um dicionário para armazenar o número total de ingressos vendidos por filme
        filmes_vendidos = {}

        # Percorre todos os ingressos no "banco de dados"
        for ingresso in Ingresso.ingressos_db:
            filme = ingresso.sessao.filme.titulo  # Obtém o título do filme
            if filme in filmes_vendidos:
                filmes_vendidos[filme] += 1  # Conta mais um ingresso vendido para o filme
            else:
                filmes_vendidos[filme] = 1  # Inicializa a contagem de ingressos vendidos

        # Ordena os filmes por número de ingressos vendidos (ordem decrescente)
        filmes_ordenados = sorted(filmes_vendidos.items(), key=lambda x: x[1], reverse=True)

        # Exibe o relatório dos filmes mais assistidos
        print("Filmes Mais Assistidos:")
        for filme, quantidade in filmes_ordenados:
            print(f"Filme: {filme}, Ingressos Vendidos: {quantidade}")
        print()

    @staticmethod
    def horariosMaisFrequentados():
        # Cria um dicionário para armazenar o número total de ingressos vendidos por horário
        horarios_vendidos = {}

        # Percorre todos os ingressos no "banco de dados"
        for ingresso in Ingresso.ingressos_db:
            horario = ingresso.sessao.horario  # Obtém o horário da sessão
            if horario in horarios_vendidos:
                horarios_vendidos[horario] += 1  # Conta mais um ingresso vendido para o horário
            else:
                horarios_vendidos[horario] = 1  # Inicializa a contagem de ingressos vendidos

        # Ordena os horários por número de ingressos vendidos (ordem decrescente)
        horarios_ordenados = sorted(horarios_vendidos.items(), key=lambda x: x[1], reverse=True)

        # Exibe o relatório dos horários mais frequentados
        print("Horários Mais Frequentados:")
        for horario, quantidade in horarios_ordenados:
            print(f"Horário: {horario}, Ingressos Vendidos: {quantidade}")
        print()

    @staticmethod
    def gerarRelatorioCompleto():
        # Gera um relatório completo dos filmes mais assistidos e dos horários mais frequentados
        print("Relatório Completo:")
        Relatorio.filmesMaisAssistidos()
        Relatorio.horariosMaisFrequentados()

#Exemplo de uso 
Relatorio.gerarRelatorioCompleto()
