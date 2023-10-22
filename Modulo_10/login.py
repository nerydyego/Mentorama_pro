from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

class LoginApp(App):
    def build(self):
        return Builder.load_file('login.kv')

    def check_login(self, username, password):
        if username == "user" and password == "password":
            return "Login successful!"
        else:
            return "Login failed. Try again."

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

    def on_login(self):
        username = self.username_input.text
        password = self.password_input.text
        result = LoginApp.get_running_app().check_login(username, password)
        self.result_label.text = result

if __name__ == "__main__":
    LoginApp().run()
