from modelos import Atividade


class AtividadeFactory:
    proximo_id = 1

    @classmethod
    def criar_atividade(
        cls,
        titulo,
        descricao,
        local,
        data,
        horario,
        limite_participantes,
        nivel_interacao
    ):
        if not titulo or not local or not data or not horario:
            raise ValueError("Título, local, data e horário são obrigatórios.")

        if limite_participantes < 2 or limite_participantes > 4:
            raise ValueError("O limite de participantes deve estar entre 2 e 4.")

        if nivel_interacao not in ["pouca conversa", "moderada", "alta interação"]:
            raise ValueError("Nível de interação inválido.")

        atividade = Atividade(
            atividade_id=cls.proximo_id,
            titulo=titulo,
            descricao=descricao,
            local=local,
            data=data,
            horario=horario,
            limite_participantes=limite_participantes,
            nivel_interacao=nivel_interacao
        )

        cls.proximo_id += 1
        return atividade