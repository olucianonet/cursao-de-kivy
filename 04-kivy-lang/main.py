
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Increment(BoxLayout):
    pass


class Test(App):
    def build(self):
        return Increment()



Test().run()
