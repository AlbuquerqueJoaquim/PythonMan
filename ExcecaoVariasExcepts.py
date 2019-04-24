
# traalhando com varias excepts em um try

def(erro):
    try:
        eval(x)
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
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
