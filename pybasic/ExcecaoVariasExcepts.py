
# tralhando com varias excepts em um try
#capturando a instancia do erro

def erro(x):
    try:
        eval(x)
    except TypeError as e:
        print("TypeError")
        print(type(e))# instancia de exceção
        print(e.args)#argumentos as mensagens
        print(e)# __str__mensagem
    except NameError as e:
        print("NameError")
        print(type(e))# instancia de exceção
        print(e.args)#argumentos as mensagens
        print(e)# __str__mensagem
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")


#TypeError
erro("int+int") # soma de duas palavras reservadas

#NameErro
erro("a") # uma variavel q não foi inicializada

#ValueError
erro("int('a')")# converção de letra para número

#ZeroDivisionError
erro("5/0") #divisão por zero
