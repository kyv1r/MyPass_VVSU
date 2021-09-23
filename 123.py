from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import requests

Builder.load_string("""
:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        GridLayout:
            rows: 2
            cols: 2
            padding: 10
            spacing: 10
            row_default_height: 30
            Label:
                text: 'Username'
            TextInput:
                id: usernamevalue
            Label:
                text: 'Password'
            TextInput:
                id: passwordvalue
                password: True
        Button:
            text: 'Login'
            on_press: root.login_button_action()

:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Failed Login'
        Button:
            text: 'Back to login'
            on_press: root.manager.current = 'login'
""")


class LoginScreen(Screen):
    def build(self):
        pass

    def login_button_action(self):
        url = 'https://reqres.in/api/login'

        # data = json.dumps({"email": "eve.holt@reqres.in","password": "cityslicka"})
        data = json.dumps({"email": self.ids.usernamevalue.text, "password": self.ids.passwordvalue.text})

        response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})

        userdata = json.loads(response.text)

        if userdata.get("token"):
            print("Logging in")
        else:
            self.manager.current = 'failedlogin'


class FailedLoginScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(FailedLoginScreen(name='failedlogin'))


class MainApp(App):

    def build(self):
        self.title = "Task Manager"
        return sm


if __name__ == '__main__':
    MainApp().run()