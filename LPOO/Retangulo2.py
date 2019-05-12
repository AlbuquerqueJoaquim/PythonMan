

class Retangulo2:

    def __init__(self, largura, altura):
        self.l = largura
        self.a = altura


    def area(self):
        return self.l * self.a

r = Retangulo2(6,3)
print(r.area())