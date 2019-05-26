
#coding: utf-8

#Trabalhando com Widgets entrada de texto

from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
    return TextInput(text="Componente de Text_input")

janela=App()
janela.build = build
janela.run()