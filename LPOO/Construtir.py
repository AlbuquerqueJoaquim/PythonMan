
# trabalhando com o construtorde objetos __init__

class A:

    def __init__(self): #utilizando construtor de objetos, self é um parametro obrigarotio que recebera a instanacia criada
        print(id(self))

a = A()
print(id(a))
