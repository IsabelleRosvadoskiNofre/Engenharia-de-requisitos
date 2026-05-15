class ServicoAtividades:
    def __init__(self):
        self.atividades = {}

    def cadastrar_atividade(self, atividade):
        self.atividades[atividade.atividade_id] = atividade
        return atividade

    def listar_atividades_disponiveis(self):
        return [
            atividade
            for atividade in self.atividades.values()
            if atividade.tem_vaga()
        ]

    def buscar_atividade_por_id(self, atividade_id):
        if atividade_id not in self.atividades:
            raise ValueError("Atividade não encontrada.")

        return self.atividades[atividade_id]

    def inscrever_usuario(self, atividade_id, usuario):
        atividade = self.buscar_atividade_por_id(atividade_id)

        if atividade.usuario_ja_inscrito(usuario.usuario_id):
            raise ValueError("Usuário já está inscrito nesta atividade.")

        if not atividade.tem_vaga():
            raise ValueError("Atividade sem vagas disponíveis.")

        atividade.participantes.append(usuario.usuario_id)

        atividade.notificar_observadores(
            f"{usuario.nome} se inscreveu na atividade '{atividade.titulo}'."
        )

        return True