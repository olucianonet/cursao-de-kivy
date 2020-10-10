
from kivy.app import App
from kivy.uix.button import Button


class Test(App):
    def buid(self):
        return Button(text="E ae mundo, firmeza?!")


Test().run()
