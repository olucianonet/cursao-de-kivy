
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Tasks(BoxLayout):
    def __init__(self, tasks, **kwargs):
        super().__init__(**kwargs)

        for task in tasks:
            self.add_widget(Label(text=task, font_size=30))


class Test(App):
    def build(self):
        return Tasks(['Estudar', 'Cortar Grama', 'Lavar o Carro'], )



Test().run()
