from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Container(GridLayout):
    pass


class MyApp(App):

    def build(self):
        self.title = 'Awesom app!!!'
        return Container()

if __name__ == "__main__":
    MyApp().run()
