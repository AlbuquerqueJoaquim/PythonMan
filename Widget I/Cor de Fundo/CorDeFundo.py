
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

#Window.clearcolor = [1, 1, 1, 1]
Window.clearcolor = get_color_from_hex("#FFFFFF")

kvcode = """

#:import C kivy.utils.get_color_from_hex

<FVerde@FloatLayout>:
    size_hint: .3, .3
    canvas.before:
        Color:
            rgba: C("#22FFAA")
        Rectangle:
            pos: self.pos
            size: self.size

FloatLayout:
    FVerde:
        pos_hiny:{"x":.4, "y":.4}

"""

class JanelaApp(App):
    def build(self):
        return  Builder.load_string( kvcode )
    pass

janela = JanelaApp()
janela.run()