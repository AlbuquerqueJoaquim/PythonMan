
# trabalhando com decorators

class A:

    def __init__(self): #metodo construtor
        self._var = 0 # deixando a variavel de acesso interno apenas

    @property # declarrando o metoto que ira retorna o valor seria o getters
    def var(self): # deixando o metodo apenas com acesso interno
        print("Valor esta sendo lido")
        return self._var

    @var.setter # incluindo o metodo setters, ira setar um valor na variavel
    def var(self, x):
        print("Valor esta sendo escrito")
        self._var = x


   # var = property(fget= _get_var,fset= _set_var)# para acessar os metotos get e set de forma externa
                                                 # atraves do property utilizando a instancia var

a = A()

a.var = 10
print(a.var)