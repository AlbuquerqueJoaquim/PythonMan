import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def funcSelf(x):
    print("FuncSelf")
Button.funcSelf = funcSelf


class MinhaTela(BoxLayout):

#funcao click

    def funcRoot(self):
        print("FuncRoot")




class Estudo5App(App):

    def funcApp(self):
        print("funcApp")


janela = Estudo5App()
janela.run()