
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tasks(ScrollView):
    def __init__(self, tasks, **kwargs):
        super().__init__(**kwargs)

        for task in tasks:
            self.ids.box.add_widget(
                Task(text=task, ))


class Task(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label1.text = text


class Test(App):
    def build(self):
        return Tasks([
            'Estudar', 'Cortar Grama', 'Lavar o Carro', 'Lavar Louça', 'Filme',
            'Organizar Finanças', 'Correr', 'Meditar',
            ], )


Test().run()
