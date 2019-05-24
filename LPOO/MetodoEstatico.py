
#trabalhando com metodos estaticos

class MEstaticos:

    @staticmethod # deixando o metodo estadico com decorators
    def func1():
        print("func1()")

    @staticmethod
    def func2(x , y):
        print("Funcao '{}' invocada.\nParams=({},{})".format("func2", x, y))

    @staticmethod
    def func3(a, b, c):
        info = """
        
        Nome da Função: {nome}
        Quantidade de Args: {quantidade}
        Args: {args}
        """
        info = info.format(
            nome=MEstaticos.func3.__name__, # retornando o nome da funcao
            quantidade=MEstaticos.func3.__code__.co_argcount,#retornando quantidade de argumentos sendo passado
            args = MEstaticos.func3.__code__.co_varnames# mostra os argumentos q estão sendo passados
        )
        print(info)

    #func1 = staticmethod(func1) # deixando o metodo como statico
    #func2 = staticmethod(func2)
    #func3 = staticmethod(func3)


me = MEstaticos()
me.func1()
me.func2(100, 200)
me.func3(5, 10, 15)