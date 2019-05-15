
# acessando os metodos get e set atraves de property
#

class A:

    def __init__(self): #metodo construtor
        self._var = 0 # deixando a variavel de acesso interno apenas

    def _get_var(self): # deixando o metodo apenas com acesso interno
        print("Valor esta sendo lido")
        return self._var

    def _set_var(self, x):
        print("Valor esta sendo escrito")
        self._var = x


    var = property(fget= _get_var,fset= _set_var)# para acessar os metotos get e set de forma externa
                                                 # atraves do property utilizando a instancia var

a = A()

a.var = 10
print(a.var)