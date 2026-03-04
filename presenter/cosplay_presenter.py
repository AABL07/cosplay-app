import re
from models.participante import Participante
from repository.participante_repo import ParticipanteRepository

class CosplayPresenter:

    def __init__(self, view, repo: ParticipanteRepository):
        self.view = view
        self.repo = repo

    def submeter(self, nome, notas_raw):
        if not nome:
            self.view.show_error("Nome é obrigatório.")
            return
        if not re.match(r"^[A-Za-zÀ-ÿ ]+$", nome):
            self.view.show_error("Nome inválido\n(somente letras e espaços).")
            return
        try:
            notas = [float(n.replace(',', '.')) for n in notas_raw]
            if any(n < 0 or n > 10 for n in notas):
                raise ValueError
        except ValueError:
            self.view.show_error("Preencha todas as notas\ncorretamente (0 a 10).")
            return

        ok, msg = self.repo.inserir(Participante(nome, notas))
        self.view.show_success(msg) if ok else self.view.show_error(msg)
        if ok:
            self.view.limpar()

    def listar(self):
        resultado = self.repo.listar_ranking()
        self.view.exibir_ranking(resultado)

    def excluir_individual(self, nome):
        if not nome:
            self.view.show_error("Informe o nome do participante.")
            return
        ok, msg = self.repo.excluir(nome)
        self.view.show_success(msg) if ok else self.view.show_error(msg)
        if ok:
            self.view.limpar_excluir()

    def excluir_todos(self):
        ok, msg = self.repo.excluir_todos()
        self.view.show_success(msg) if ok else self.view.show_error(msg)
