
#Utilizando os metodos getters e setters (encapsulamento) de dados


class Retangulo:

    def __init__(self, largura, altura):
        self.largura = 0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)


    def set_altura(self, num):
        if (not(isinstance(num, int)and(num >0))): #criando uma regra para dados de entrada na variavel
            raise ValueError("Valor inválido para Altura: {}".format(num)) #informando o possivel excesao
        self.altura = num

    def set_largura(self, num):
        if (not(isinstance(num, int)and(num > 0))):
            raise ValueError("Valor inválido para Largura: {}".format(num))

        self.largura = num

    def get_area(self):
        return self.altura * self.largura



r = Retangulo(largura=9, altura=10)