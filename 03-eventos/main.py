
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Test(App):
    def build(self):
        box1 = BoxLayout(orientation='vertical')
        button1 = Button(text="Add", font_size=30, on_release=self.increment)
        self.label1 = Label(text="0", font_size=30)
        box1.add_widget(button1)
        box1.add_widget(self.label1)

        return box1

    def increment(self, button):
        self.label1.text = str(int(self.label1.text) + 1)


Test().run()
