

#coding: utf-8

#Trabalhando com novas propriedades de um Widgets e importando classes da biblioteca kivy

from kivy.app import App
from kivy.uix.label import Label

def build():
    lb = Label()
    lb.text = "Curso de Python e Kivy"
    lb.italic=True
    lb.font_size= 60
    return lb


app = App()
app.build = build
app.run()
