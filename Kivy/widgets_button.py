
#coding: utf-8
#Trabalhando com outros Widgets, e utilizando um evento ao clicar no button

from kivy.app import App
from kivy.uix.button import Button

def click():
    print("O Boao foi clicado!")

def build():
    bt = Button(text="Clique aqui!")
    bt.on_press = click # associando o evendo on_press a função click
    return bt


janela = App()
janela.build = build
janela.run()