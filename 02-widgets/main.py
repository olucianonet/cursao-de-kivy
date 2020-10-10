
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Test(App):
    def build(self):
        box1 = BoxLayout(orientation='vertical')
        button1 = Button(text="Button 1")
        label1 = Label(text="Label 1")
        box1.add_widget(button1)
        box1.add_widget(label1)

        box2 = BoxLayout()
        button2 = Button(text="Button 2")
        label2 = Label(text="Label 1")
        box2.add_widget(button2)
        box2.add_widget(label2)

        box1.add_widget(box2)

        return box1


Test().run()
