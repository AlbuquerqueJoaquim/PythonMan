

import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):

#funcao click

    def click(self):
        print("Hello Word!!")
        #acessando os labels pela funcao click
        self.ids.lb1.text = "Hello Word!!"
        self.ids.lb2.text = "kivy e Python é vida!!"


class Estudo4App(App):
    pass

janela = Estudo4App()
janela.run()