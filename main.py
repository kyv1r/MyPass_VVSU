from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window

Window.fullscreen = False

Window.size = (320, 600)


class MainApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        # Set App Title
        self.title = "MyPass"

        # Load kv screen files to builder
        screen_manager.add_widget(Builder.load_file("splashScreen.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))

        # Return screen manager
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 5)  # Delay for 10 seconds

    def change_screen(self, dt):
        screen_manager.current = "MainScreen"


########################################################################
## RUN APP
########################################################################      
MainApp().run()
########################################################################
## END ==>
########################################################################
