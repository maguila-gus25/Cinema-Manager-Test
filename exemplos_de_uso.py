
#Exemplo de Uso 1: Adicionar um Filme

filme1 = Filme(titulo="O Poderoso Chefão", duracao="2h55min", genero="Drama", classificacao_etaria=18, sinopse="A saga da família Corleone.")
resultado = filme1.adicionarFilme()
print(resultado)

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


