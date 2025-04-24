from database import init_db
from filme import Filme
from sala import Sala
from sessao import Sessao
from ingresso import Ingresso
from cliente import Cliente
from venda import Venda
from datetime import datetime, timedelta
import traceback
import sqlite3

def inicializar_sistema():
    try:
        init_db()
        print("Sistema inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar o sistema: {e}")
        traceback.print_exc()

def criar_filmes_exemplo():
    try:
        filmes = [
            Filme("O Poderoso Chefão", 175, "Drama", "18", "A saga da família Corleone"),
            Filme("Interestelar", 169, "Ficção Científica", "12", "Uma jornada épica através do espaço e tempo"),
            Filme("Toy Story", 81, "Animação", "L", "As aventuras dos brinquedos de Andy"),
            Filme("O Senhor dos Anéis: A Sociedade do Anel", 178, "Aventura", "12", "Uma jornada para destruir o Um Anel")
        ]
        
        saved_filmes = []
        for filme in filmes:
            filme.adicionar_filme()
            print(f"Criado filme: {filme.titulo} (ID: {filme.id})")
            saved_filmes.append(filme)
        return saved_filmes
    except Exception as e:
        print(f"Erro ao criar filmes: {e}")
        traceback.print_exc()
        return []

def criar_salas_exemplo():
    try:
        salas = [
            Sala(1, "2D", 100),
            Sala(2, "3D", 80),
            Sala(3, "IMAX", 120),
            Sala(4, "2D", 90)
        ]
        
        for sala in salas:
            print(f"Tentando adicionar sala {sala.numero}...")
            sala.criar_sala()
            print(f"Criada sala: {sala.numero} - {sala.tipo}")
            
            print(f"Adicionando assentos para sala {sala.numero}...")
            # Adicionar assentos para cada sala
            for fileira in ['A', 'B', 'C', 'D', 'E']:
                for numero in range(1, 21):
                    try:
                        sala.adicionar_assento(fileira, numero)
                    except Exception as e:
                        print(f"Erro ao adicionar assento {fileira}{numero} na sala {sala.numero}: {e}")
                        traceback.print_exc()
            print(f"Adicionados assentos à sala {sala.numero}")
        return salas
    except Exception as e:
        print(f"Erro ao criar salas: {e}")
        traceback.print_exc()
        return []

def criar_sessoes_exemplo(filmes, salas):
    try:
        hoje = datetime.now()
        sessoes = []
        
        # Criar sessões para os próximos 3 dias
        for dia in range(3):
            data = (hoje + timedelta(days=dia)).strftime('%Y-%m-%d')
            
            # Verificar se temos filmes e salas suficientes
            if len(filmes) < 4 or len(salas) < 4:
                print("Erro: Número insuficiente de filmes ou salas")
                return []
            
            # Sessões para o Poderoso Chefão
            sessoes.append(Sessao(filmes[0].id, salas[0].id, "14:00", data, 100))
            sessoes.append(Sessao(filmes[0].id, salas[0].id, "19:00", data, 100))
            
            # Sessões para Interestelar
            sessoes.append(Sessao(filmes[1].id, salas[1].id, "15:30", data, 80))
            sessoes.append(Sessao(filmes[1].id, salas[1].id, "20:30", data, 80))
            
            # Sessões para Toy Story
            sessoes.append(Sessao(filmes[2].id, salas[2].id, "13:00", data, 120))
            sessoes.append(Sessao(filmes[2].id, salas[2].id, "16:00", data, 120))
            
            # Sessões para O Senhor dos Anéis
            sessoes.append(Sessao(filmes[3].id, salas[3].id, "17:00", data, 90))
            sessoes.append(Sessao(filmes[3].id, salas[3].id, "21:00", data, 90))
        
        saved_sessoes = []
        for sessao in sessoes:
            try:
                print(f"Tentando criar sessão para filme {sessao.filme_id} na sala {sessao.sala_id}...")
                sessao.criar_sessao()
                print(f"Criada sessão: {sessao.data} {sessao.horario} (ID: {sessao.id})")
                saved_sessoes.append(sessao)
            except Exception as e:
                print(f"Erro ao criar sessão: {e}")
                traceback.print_exc()
        return saved_sessoes
    except Exception as e:
        print(f"Erro ao criar sessões: {e}")
        traceback.print_exc()
        return []

def exemplo_vendas(filmes, salas, sessoes):
    try:
        # Criar alguns clientes
        clientes = [
            Cliente("João Silva", "joao@email.com", "123456789"),
            Cliente("Maria Santos", "maria@email.com", "987654321"),
            Cliente("Pedro Oliveira", "pedro@email.com", "456789123")
        ]
        
        for cliente in clientes:
            try:
                cliente.save()
                print(f"Criado cliente: {cliente.nome} (ID: {cliente.id})")
            except Exception as e:
                print(f"Erro ao criar cliente {cliente.nome}: {e}")
                traceback.print_exc()
        
        # Realizar algumas vendas
        for sessao in sessoes[:6]:  # Vamos vender ingressos para as primeiras 6 sessões
            try:
                print(f"\nProcessando vendas para sessão {sessao.id}...")
                assentos_disponiveis = sessao.get_assentos_disponiveis()
                print(f"Assentos disponíveis: {len(assentos_disponiveis)}")
                
                if assentos_disponiveis:
                    # Vender 3 ingressos para cada sessão
                    for j in range(3):
                        if j < len(assentos_disponiveis):
                            try:
                                assento = assentos_disponiveis[j]
                                cliente = clientes[j % len(clientes)]
                                
                                # Criar e vender ingresso
                                print(f"Criando ingresso para assento {assento['fileira']}{assento['numero']}...")
                                ingresso = Ingresso(sessao.id, assento['id'], 30.00)
                                ingresso.save()
                                print(f"Emitindo ingresso {ingresso.id}...")
                                ingresso.emitir_ingresso()
                                
                                # Registrar venda
                                print(f"Registrando venda para cliente {cliente.nome}...")
                                venda = Venda(cliente.id, ingresso.id, "cartão de crédito", 30.00)
                                resultado_venda = venda.registrar_venda()
                                print(resultado_venda)
                                
                                # Buscar informações atualizadas
                                filme = Filme.get_by_id(sessao.filme_id)
                                if filme is None:
                                    print(f"Aviso: Não foi possível encontrar o filme com ID {sessao.filme_id}")
                                    continue
                                    
                                sala = Sala.get_by_id(sessao.sala_id)
                                if sala is None:
                                    print(f"Aviso: Não foi possível encontrar a sala com ID {sessao.sala_id}")
                                    continue
                                
                                print(f"\nVenda realizada:")
                                print(f"Cliente: {cliente.nome}")
                                print(f"Filme: {filme.titulo}")
                                print(f"Sala: {sala.numero}")
                                print(f"Data: {sessao.data} {sessao.horario}")
                                print(f"Assento: {assento['fileira']}{assento['numero']}")
                                print(f"Preço: R$30.00")
                                
                                # Atualizar ingressos disponíveis
                                sessao.ingressos_disponiveis -= 1
                                sessao.save()
                            except Exception as e:
                                print(f"Erro ao processar venda: {e}")
                                traceback.print_exc()
            except Exception as e:
                print(f"Erro ao processar sessão {sessao.id}: {e}")
                traceback.print_exc()
    except Exception as e:
        print(f"Erro ao realizar vendas: {e}")
        traceback.print_exc()

def exemplo_uso():
    try:
        print("\n=== Criando Filmes ===")
        filmes = criar_filmes_exemplo()
        
        if not filmes:
            print("Erro ao criar filmes. Encerrando execução.")
            return
        
        print("\n=== Criando Salas ===")
        salas = criar_salas_exemplo()
        
        if not salas:
            print("Erro ao criar salas. Encerrando execução.")
            return
        
        print("\n=== Criando Sessões ===")
        sessoes = criar_sessoes_exemplo(filmes, salas)
        
        if not sessoes:
            print("Erro ao criar sessões. Encerrando execução.")
            return
        
        print("\n=== Realizando Vendas ===")
        exemplo_vendas(filmes, salas, sessoes)
        
        print("\n=== Exemplo Completo Concluído ===")
    except Exception as e:
        print(f"Erro na execução do exemplo: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    try:
        # Remover banco de dados existente para começar do zero
        import os
        if os.path.exists('cinema.db'):
            os.remove('cinema.db')
            print("Banco de dados anterior removido.")
        
        inicializar_sistema()
        exemplo_uso()
    except Exception as e:
        print(f"Erro fatal: {e}")
        traceback.print_exc() 