from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Container(GridLayout):
    pass


class MyMain(App):

    def build(self):
        self.title = 'сука!!'
        return Container()

if __name__ == "__main__":
    MyMain().run()
