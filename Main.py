import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

kivy.require("2.1.0")


class Layout(GridLayout):
    def __init__(self, **kwargs):
        self.cols = 1
        super(Layout, self).__init__(**kwargs)
        self.editor = TextInput()
        self.add_widget(self.editor)


class Main(App):
    def build(self):
        return Layout()


if __name__ == "__main__":
    Main().run()
