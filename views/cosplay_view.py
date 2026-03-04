from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from repository.participante_repo import ParticipanteRepository
from presenter.cosplay_presenter import CosplayPresenter


def show_popup(title, message):
    content = BoxLayout(orientation='vertical', padding=10, spacing=10)
    content.add_widget(Label(text=message))
    btn = Button(text='OK', size_hint=(1, None), height=44)
    popup = Popup(title=title, content=content, size_hint=(0.85, 0.4))
    btn.bind(on_press=popup.dismiss)
    content.add_widget(btn)
    popup.open()


class CosplayView(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=12, spacing=8, **kwargs)
        repo = ParticipanteRepository()
        repo.criar_tabela()
        self.presenter = CosplayPresenter(view=self, repo=repo)
        self._build_ui()

    def _build_ui(self):
        # Nome
        self.add_widget(Label(text='Nome do participante:', size_hint=(1, None), height=28))
        self.nome_input = TextInput(hint_text='Nome', multiline=False, size_hint=(1, None), height=42)
        self.add_widget(self.nome_input)

        # Notas por critério (3 juízes cada)
        self.campos_notas = []
        for criterio in ['Fidelidade', 'Complexidade', 'Acabamento']:
            row = BoxLayout(orientation='horizontal', size_hint=(1, None), height=44, spacing=6)
            row.add_widget(Label(text=criterio + ':', size_hint=(0.38, 1)))
            for j in range(3):
                inp = TextInput(
                    hint_text=f'J{j+1}',
                    multiline=False,
                    input_filter='float',
                    size_hint=(0.20, 1)
                )
                row.add_widget(inp)
                self.campos_notas.append(inp)
            self.add_widget(row)

        # Botões principais
        btn_row = BoxLayout(orientation='horizontal', size_hint=(1, None), height=48, spacing=6)
        for text, action in [('Submeter', self.on_submeter), ('Ranking', self.on_listar), ('Limpar', self.limpar)]:
            btn = Button(text=text)
            btn.bind(on_press=action)
            btn_row.add_widget(btn)
        self.add_widget(btn_row)

        # Exclusão individual
        del_row = BoxLayout(orientation='horizontal', size_hint=(1, None), height=44, spacing=6)
        self.excluir_input = TextInput(hint_text='Nome para excluir', multiline=False)
        btn_del = Button(text='Excluir', size_hint=(0.32, 1))
        btn_del.bind(on_press=self.on_excluir_individual)
        del_row.add_widget(self.excluir_input)
        del_row.add_widget(btn_del)
        self.add_widget(del_row)

        # Excluir todos
        btn_todos = Button(text='Excluir Todos', size_hint=(1, None), height=44)
        btn_todos.bind(on_press=self.on_confirmar_excluir_todos)
        self.add_widget(btn_todos)
        self.add_widget(Widget(size_hint_y=1))

    # ===================== EVENTOS =====================

    def on_submeter(self, *_):
        self.presenter.submeter(
            self.nome_input.text.strip(),
            [e.text for e in self.campos_notas]
        )

    def on_listar(self, *_):
        self.presenter.listar()

    def on_excluir_individual(self, *_):
        self.presenter.excluir_individual(self.excluir_input.text.strip())

    def on_confirmar_excluir_todos(self, *_):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='Deseja apagar todos os dados?'))
        btn_row = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=44)
        btn_sim = Button(text='Sim')
        btn_nao = Button(text='Não')
        btn_row.add_widget(btn_sim)
        btn_row.add_widget(btn_nao)
        content.add_widget(btn_row)
        popup = Popup(title='Confirmar', content=content, size_hint=(0.8, 0.38))

        def confirmar(_):
            popup.dismiss()
            self.presenter.excluir_todos()

        btn_sim.bind(on_press=confirmar)
        btn_nao.bind(on_press=popup.dismiss)
        popup.open()

    # ===================== INTERFACE (chamados pelo Presenter) =====================

    def show_error(self, msg):
        show_popup("Erro", msg)

    def show_success(self, msg):
        show_popup("Sucesso", msg)

    def limpar(self, *_):
        self.nome_input.text = ''
        for campo in self.campos_notas:
            campo.text = ''
        self.excluir_input.text = ''

    def limpar_excluir(self):
        self.excluir_input.text = ''

    def exibir_ranking(self, resultado):
        if not resultado:
            show_popup("Ranking", "Nenhum participante cadastrado.")
            return

        ranking_text = "\n".join(
            [f"{i+1}º - {nome}: {media:.2f}" for i, (nome, media) in enumerate(resultado)]
        )
        content = BoxLayout(orientation='vertical', padding=10, spacing=8)
        scroll = ScrollView()
        lbl = Label(text=f"🏅 Ranking 🏅\n\n{ranking_text}", size_hint_y=None, halign='center')
        lbl.bind(texture_size=lbl.setter('size'))
        scroll.add_widget(lbl)
        content.add_widget(scroll)
        btn = Button(text='OK', size_hint=(1, None), height=44)
        popup = Popup(title='Ranking', content=content, size_hint=(0.9, 0.75))
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.open()
