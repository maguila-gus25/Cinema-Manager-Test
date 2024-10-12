class SalaVisao:
    def __init__(self, controlador):
        self.controlador = controlador

    def menu_principal(self):
        while True:
            print("\n===== Sistema de Gerenciamento de Salas =====")
            print("1. Adicionar Sala")
            print("2. Atualizar Sala")
            print("3. Remover Sala")
            print("4. Listar Salas")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_sala()
            elif opcao == "2":
                self.atualizar_sala()
            elif opcao == "3":
                self.remover_sala()
            elif opcao == "4":
                self.listar_salas()
            elif opcao == "5":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def adicionar_sala(self):
        numero = int(input("Digite o número da sala: "))
        capacidade = int(input("Digite a capacidade da sala: "))
        tipo = input("Digite o tipo da sala (2D, 3D, IMAX): ")
        resultado = self.controlador.adicionar_sala(numero, capacidade, tipo)
        print(resultado)

    def atualizar_sala(self):
        numero = int(input("Digite o número da sala a ser atualizada: "))
        capacidade = input("Digite a nova capacidade (ou deixe em branco para não alterar): ")
        tipo = input("Digite o novo tipo (ou deixe em branco para não alterar): ")

        # Converte os valores para None se estiverem em branco
        capacidade = int(capacidade) if capacidade else None
        tipo = tipo if tipo else None

        resultado = self.controlador.atualizar_sala(numero, capacidade, tipo)
        print(resultado)

    def remover_sala(self):
        numero = int(input("Digite o número da sala a ser removida: "))
        resultado = self.controlador.remover_sala(numero)
        print(resultado)

    def listar_salas(self):
        salas = self.controlador.listar_salas()
        if isinstance(salas, list):
            print("\nSalas cadastradas:")
            for sala in salas:
                print(sala)
        else:
            print(salas)
