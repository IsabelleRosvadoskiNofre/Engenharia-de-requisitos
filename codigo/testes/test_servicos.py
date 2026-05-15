import unittest
import sys
import os

# Permite importar os arquivos da pasta codigo/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modelos import Usuario
from fabrica import AtividadeFactory
from servicos import ServicoAtividades


class TestAtividadeFactory(unittest.TestCase):

    def setUp(self):
        # Reinicia o contador para deixar os testes previsíveis
        AtividadeFactory.proximo_id = 1

    def test_criar_atividade_com_sucesso(self):
        atividade = AtividadeFactory.criar_atividade(
            titulo="Caminhada no parque",
            descricao="Caminhada leve em grupo pequeno",
            local="Parque Jaboti",
            data="20/05/2026",
            horario="16:00",
            limite_participantes=4,
            nivel_interacao="pouca conversa"
        )

        self.assertEqual(atividade.titulo, "Caminhada no parque")
        self.assertEqual(atividade.local, "Parque Jaboti")
        self.assertEqual(atividade.limite_participantes, 4)
        self.assertEqual(atividade.nivel_interacao, "pouca conversa")
        self.assertEqual(atividade.participantes, [])

    def test_criar_atividade_com_limite_invalido_deve_gerar_erro(self):
        with self.assertRaises(ValueError):
            AtividadeFactory.criar_atividade(
                titulo="Aula de violão",
                descricao="Aula experimental",
                local="Escola de música",
                data="21/05/2026",
                horario="14:00",
                limite_participantes=8,
                nivel_interacao="moderada"
            )

    def test_criar_atividade_com_limite_minimo_valido(self):
        atividade = AtividadeFactory.criar_atividade(
            titulo="Estudo em biblioteca",
            descricao="Grupo pequeno para estudar em silêncio",
            local="Biblioteca Municipal",
            data="22/05/2026",
            horario="10:00",
            limite_participantes=2,
            nivel_interacao="pouca conversa"
        )

        self.assertEqual(atividade.limite_participantes, 2)
        self.assertTrue(atividade.tem_vaga())


class TestServicoAtividades(unittest.TestCase):

    def setUp(self):
        AtividadeFactory.proximo_id = 1

        self.servico = ServicoAtividades()

        self.usuario = Usuario(
            usuario_id=1,
            nome="Ana",
            interesses=["caminhada", "música"],
            preferencia_comunicacao="moderada"
        )

        self.atividade = AtividadeFactory.criar_atividade(
            titulo="Caminhada no parque",
            descricao="Caminhada leve",
            local="Parque Jaboti",
            data="20/05/2026",
            horario="16:00",
            limite_participantes=2,
            nivel_interacao="pouca conversa"
        )

        self.servico.cadastrar_atividade(self.atividade)

    def test_inscrever_usuario_com_sucesso(self):
        resultado = self.servico.inscrever_usuario(
            atividade_id=self.atividade.atividade_id,
            usuario=self.usuario
        )

        self.assertTrue(resultado)
        self.assertIn(self.usuario.usuario_id, self.atividade.participantes)

    def test_inscrever_usuario_em_atividade_inexistente_deve_gerar_erro(self):
        with self.assertRaises(ValueError):
            self.servico.inscrever_usuario(
                atividade_id=999,
                usuario=self.usuario
            )

    def test_inscrever_usuario_em_atividade_no_limite_de_vagas(self):
        usuario_2 = Usuario(
            usuario_id=2,
            nome="Bruno",
            interesses=["caminhada"],
            preferencia_comunicacao="pouca conversa"
        )

        self.servico.inscrever_usuario(self.atividade.atividade_id, self.usuario)
        self.servico.inscrever_usuario(self.atividade.atividade_id, usuario_2)

        self.assertFalse(self.atividade.tem_vaga())
        self.assertEqual(len(self.atividade.participantes), 2)

    def test_inscrever_usuario_duplicado_deve_gerar_erro(self):
        self.servico.inscrever_usuario(self.atividade.atividade_id, self.usuario)

        with self.assertRaises(ValueError):
            self.servico.inscrever_usuario(
                atividade_id=self.atividade.atividade_id,
                usuario=self.usuario
            )


if __name__ == "__main__":
    unittest.main()