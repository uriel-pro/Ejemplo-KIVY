from kivy.app import App
from kivy.uix.label import Label


class MiApp(App):
    def build(self):
        return Label(text="¡hola desde Kivy!")



MiApp().run()