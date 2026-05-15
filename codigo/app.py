from modelos import Usuario
from fabrica import AtividadeFactory
from servicos import ServicoAtividades
from notificadores import NotificadorConsole


def exibir_atividade(atividade):
    print(f"\nID: {atividade.atividade_id}")
    print(f"Título: {atividade.titulo}")
    print(f"Descrição: {atividade.descricao}")
    print(f"Local: {atividade.local}")
    print(f"Data: {atividade.data}")
    print(f"Horário: {atividade.horario}")
    print(f"Nível de interação: {atividade.nivel_interacao}")
    print(f"Participantes: {len(atividade.participantes)}/{atividade.limite_participantes}")


def main():
    servico = ServicoAtividades()

    usuario_logado = Usuario(
        usuario_id=1,
        nome="Isabelle",
        interesses=["caminhada", "música", "estudo"],
        preferencia_comunicacao="moderada"
    )

    while True:
        print("\n=== Conecta ND ===")
        print("1 - Criar atividade")
        print("2 - Listar atividades disponíveis")
        print("3 - Inscrever-se em uma atividade")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                titulo = input("Título da atividade: ")
                descricao = input("Descrição: ")
                local = input("Local: ")
                data = input("Data: ")
                horario = input("Horário: ")

                print("\nNíveis de interação:")
                print("- pouca conversa")
                print("- moderada")
                print("- alta interação")
                nivel_interacao = input("Nível de interação: ")

                limite = int(input("Limite de participantes entre 2 e 4: "))

                atividade = AtividadeFactory.criar_atividade(
                    titulo=titulo,
                    descricao=descricao,
                    local=local,
                    data=data,
                    horario=horario,
                    limite_participantes=limite,
                    nivel_interacao=nivel_interacao
                )

                atividade.adicionar_observador(NotificadorConsole())
                servico.cadastrar_atividade(atividade)

                print("\nAtividade criada com sucesso!")

            except ValueError as erro:
                print(f"\nErro: {erro}")

        elif opcao == "2":
            atividades = servico.listar_atividades_disponiveis()

            if not atividades:
                print("\nNenhuma atividade disponível no momento.")
            else:
                print("\nAtividades disponíveis:")
                for atividade in atividades:
                    exibir_atividade(atividade)

        elif opcao == "3":
            try:
                atividade_id = int(input("Informe o ID da atividade: "))
                servico.inscrever_usuario(atividade_id, usuario_logado)
                print("\nInscrição realizada com sucesso!")

            except ValueError as erro:
                print(f"\nErro: {erro}")

        elif opcao == "0":
            print("Encerrando sistema.")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    main()