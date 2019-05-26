
#coding: utf-8

# importando classes da biblioteca grafica kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

def click():
    print(ed.text) # imprimindo o que esta sendo digitado

def build():

    layout = FloatLayout()
    global ed # essa não e uma boa pratica de progamação
    ed = TextInput(text="Digite")
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 60
    ed.y = 250

    bt = Button(text="Clique Aqui!")
    bt.size_hint = None, None
    bt.height = 100
    bt.width = 100
    bt.y = 150
    bt.x = 170

    bt.on_press = click
    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout
janela = App()
janela.title = "Primeira Janela com Button e campo texto" # titulo da nossa janela
from kivy.core.window import Window # definindo o tamanho da nossa janela
Window.size = 600, 600

janela.build = build
janela.run()
