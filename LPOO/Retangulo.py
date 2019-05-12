


class Retangulo:

    def __init__(self):# inicializando as variaveis com o valor 0
        self.a = 0
        self.l = 0
    def area(self):
        return self.a * self.l # calculando a area

r1 = Retangulo() # fazendo a instancia de retangulo

r1.l = 10
r1.a = 5

print(r1.area())