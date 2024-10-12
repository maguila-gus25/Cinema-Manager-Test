
#Exemplo de Uso 1: Adicionar um Filme

# Criação de vários filmes usando a classe Filme

filme1 = Filme(titulo="O Poderoso Chefão", duracao="2h55min", genero="Drama", classificacao_etaria=18, sinopse="A saga da família Corleone.")
filme2 = Filme(titulo="Vingadores: Ultimato", duracao="3h", genero="Ação", classificacao_etaria=12, sinopse="Os heróis da Marvel enfrentam Thanos em uma batalha épica.")
filme3 = Filme(titulo="Matrix", duracao="2h16min", genero="Ficção Científica", classificacao_etaria=14, sinopse="Um hacker descobre a verdade sobre sua realidade e o papel que ele desempenha.")
filme4 = Filme(titulo="A Origem", duracao="2h28min", genero="Suspense", classificacao_etaria=14, sinopse="Um especialista em invadir sonhos embarca em uma missão perigosa.")
filme5 = Filme(titulo="Coringa", duracao="2h02min", genero="Drama", classificacao_etaria=16, sinopse="A história da transformação de Arthur Fleck no icônico vilão Coringa.")
filme6 = Filme(titulo="Toy Story 4", duracao="1h40min", genero="Animação", classificacao_etaria=L, sinopse="Woody e seus amigos embarcam em mais uma aventura, agora com o novo brinquedo Forky.")
filme7 = Filme(titulo="Parasita", duracao="2h12min", genero="Suspense", classificacao_etaria=16, sinopse="A história de duas famílias, uma rica e uma pobre, que se entrelaçam de maneira perigosa.")
filme8 = Filme(titulo="Star Wars: O Despertar da Força", duracao="2h18min", genero="Ficção Científica", classificacao_etaria=12, sinopse="Uma nova geração de heróis luta contra a Primeira Ordem.")
filme9 = Filme(titulo="Titanic", duracao="3h15min", genero="Romance", classificacao_etaria=12, sinopse="Uma história de amor durante a fatídica viagem do Titanic.")
filme10 = Filme(titulo="Jurassic Park", duracao="2h7min", genero="Aventura", classificacao_etaria=10, sinopse="Cientistas recriam dinossauros, mas o parque não sai como o esperado.")

filme1.adicionarFilme()
filme2.adicionarFilme()
filme3.adicionarFilme()
filme4.adicionarFilme()
filme5.adicionarFilme()
filme6.adicionarFilme()
filme7.adicionarFilme()
filme8.adicionarFilme()
filme9.adicionarFilme()
filme10.adicionarFilme()

#Criando Sessoes

sessao1 = Sessao(filme=filme1, sala=Sala(1, 100, "2D"), horario="14:00", ingressos_disponiveis=100)
sessao2 = Sessao(filme=filme2, sala=Sala(2, 50, "VIP"), horario="19:00", ingressos_disponiveis=50)
sessao3 = Sessao(filme=filme3, sala=Sala(1, 100, "2D"), horario="14:00", ingressos_disponiveis=100)
sessao4 = Sessao(filme=filme4, sala=Sala(2, 50, "VIP"), horario="19:00", ingressos_disponiveis=50)
sessao5 = Sessao(filme=filme5, sala=Sala(1, 100, "2D"), horario="14:00", ingressos_disponiveis=100)
sessao6 = Sessao(filme=filme6, sala=Sala(2, 50, "VIP"), horario="19:00", ingressos_disponiveis=50)
sessao7 = Sessao(filme=filme7, sala=Sala(1, 100, "2D"), horario="14:00", ingressos_disponiveis=100)
sessao8 = Sessao(filme=filme8, sala=Sala(2, 50, "VIP"), horario="19:00", ingressos_disponiveis=50)
sessao9 = Sessao(filme=filme9, sala=Sala(1, 100, "2D"), horario="14:00", ingressos_disponiveis=100)
sessao10 = Sessao(filme=filme10, sala=Sala(2, 50, "VIP"), horario="19:00", ingressos_disponiveis=50)

sessao1.adicionarSessao()
sessao2.adicionarSessao()
sessao3.adicionarSessao()
sessao4.adicionarSessao()
sessao5.adicionarSessao()
sessao6.adicionarSessao()
sessao7.adicionarSessao()
sessao8.adicionarSessao()
sessao9.adicionarSessao()
sessao10.adicionarSessao()

sala1 = Sala(numero=1, capacidade=100, tipo="3D")
sala2 = Sala(numero=2, capacidade=50, tipo="VIP")
sala3 = Sala(numero=3, capacidade=100, tipo="2D")
sala4 = Sala(numero=4, capacidade=50, tipo="VIP")
sala5 = Sala(numero=5, capacidade=100, tipo="3D")
sala6 = Sala(numero=6, capacidade=50, tipo="VIP")
sala7 = Sala(numero=7, capacidade=100, tipo="2D")
sala8 = Sala(numero=8, capacidade=50, tipo="VIP")
sala9 = Sala(numero=9, capacidade=100, tipo="3D")
sala10 = Sala(numero=10, capacidade=50, tipo="VIP")

sala1 = adicionarSala()
sala2 = adicionarSala()
sala3 = adicionarSala()
sala4 = adicionarSala()
sala5 = adicionarSala()
sala6 = adicionarSala()
sala7 = adicionarSala()
sala8 = adicionarSala()
sala9 = adicionarSala()
sala10 = adicionarSala()



#Exemplo de Uso 2: Atualizar um Filme

filme1.atualizarFilme(titulo="O Poderoso Chefão - Parte I", duracao="3h", sinopse="Atualizada sinopse da saga da família Corleone.")
print(filme1)

#Exemplo de Uso 3: Registrar Venda de Ingressos

cliente1 = Cliente(nome="João Silva", fone="123456789", email="joao@example.com", historico_compras=None)
sessao1 = Sessao(filme=filme1, sala=Sala(1, 100, "3D"), data="20/10/2024", horario="19:00", ingressos_disponiveis=100)
ingresso1 = Ingresso(sessao=sessao1, assento="A1", preco=30.00)
ingresso2 = Ingresso(sessao=sessao1, assento="A2", preco=30.00)
venda = Venda(cliente=cliente1, ingressos=[ingresso1, ingresso2], metodo_de_pagamento="cartão de crédito")
venda.registrarVenda()

#Exemplo de Uso 4: Gerar Recibo de Venda

recibo = venda.gerarRecibo()
print(recibo)

#Exemplo de Uso 5: Adicionar Sala

sala1 = Sala(numero=1, capacidade=100, tipo="3D")
resultado = sala1.adicionarSala()
print(resultado)

#Exemplo de Uso 6: Remover Cliente

resultado_remover_cliente = cliente1.removerCliente()
print(resultado_remover_cliente)

================================================================


sala1 = Sala(1, 100, "3D")
print(20*"=")
print(sala1.adicionarSala())

filme1 = Filme("Inception", "148 min", "Sci-Fi", 14, "Um ladrão especializado em extrair segredos do subconsciente das pessoas é oferecido a chance de ter sua vida de volta, se ele conseguir realizar uma tarefa impossível: plantar uma ideia na mente de um CEO.")
print(20*"=")
print(filme1.adicionarFilme())

sessao1 = Sessao(filme1, sala1, "11/09/2024", "17h30", "43")
print(20*"=")
print(sessao1.adicionarSessao())
print(20*"=")
print(sala1)
print(20*"=")
print(sessao1.removerSessao())

cliente1 = Cliente("Gustavo Ramos", "(48)98456-6284", "gustavohcramos@gmail.com", "")
print(cliente1)

print(cliente1.cadastrarCliente())
print(cliente1.atualizarCliente("Felipe Ramos", "(48)98484-3030", "felipebcramos@gmail.com", ""))

print(cliente1.removerCliente())


ingresso = Ingresso(sessao1, assento="A1", preco=30.0)


print(ingresso.verificarDisponibilidade())  # True
ingresso.emitirIngresso()  # Vende o ingresso
print(ingresso.verificarDisponibilidade())  # False
ingresso.cancelarIngresso()  # Cancela o ingresso


