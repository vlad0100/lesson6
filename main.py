from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

import ast


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class AppWindow(Screen):
    pass


class Main(MDApp):
    def build(self):
        self.screen = FirstWindow

        return Builder.load_file("Registration.kv")

    def log_in(self, password, user):
        with open('database.txt') as f:
            data = f.read()

        database = ast.literal_eval(data)

        if user not in database:
            database.update({user: password})

            with open('database.txt', 'w') as data:
                data.write(str(database))

            self.root.current = "AppWindow"

    def sign_up(self, password, user):
        with open('database.txt') as f:
            data = f.read()

        database = ast.literal_eval(data)

        if user in database:
            if database[user] == password:
                self.root.current = "AppWindow"


if __name__ == '__main__':
    Main().run()
