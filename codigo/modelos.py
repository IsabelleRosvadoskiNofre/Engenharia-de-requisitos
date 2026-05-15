class Usuario:
    def __init__(self, usuario_id, nome, interesses=None, preferencia_comunicacao="moderada"):
        self.usuario_id = usuario_id
        self.nome = nome
        self.interesses = interesses or []
        self.preferencia_comunicacao = preferencia_comunicacao


class Atividade:
    def __init__(
        self,
        atividade_id,
        titulo,
        descricao,
        local,
        data,
        horario,
        limite_participantes,
        nivel_interacao
    ):
        self.atividade_id = atividade_id
        self.titulo = titulo
        self.descricao = descricao
        self.local = local
        self.data = data
        self.horario = horario
        self.limite_participantes = limite_participantes
        self.nivel_interacao = nivel_interacao
        self.participantes = []
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, mensagem):
        for observador in self.observadores:
            observador.atualizar(mensagem)

    def tem_vaga(self):
        return len(self.participantes) < self.limite_participantes

    def usuario_ja_inscrito(self, usuario_id):
        return usuario_id in self.participantes