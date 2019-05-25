
#coding:utf-8

#criando a primeira app com kivy

from kivy.app import App
from kivy.uix.label import Label

#criando uma função para retorna um label com a frase hello word
def build():
    return Label(text = "Hello Word")

hello_word = App() #realizando instancia de App
hello_word.build = build
hello_word.run() # rodando
