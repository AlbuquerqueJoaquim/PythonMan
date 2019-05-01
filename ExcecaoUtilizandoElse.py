
#utilizando else

def erro(x):
    try:
        eval(x)
    except TypeError as e:
        print("TypeError")

    except NameError as e:
        print("NameError")

    except ValueError:
        print("ValueError")

    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print("Nenhuma exeção ocorreu!!")


#TypeError
erro("int+int") # soma de duas palavras reservadas

#NameErro
erro("a") # uma variavel q não foi inicializada

#ValueError
erro("int('a')")# converção de letra para número

#ZeroDivisionError
erro("5/0") #divisão por zero

erro("10+10") #nenhuma exceção
print("Aplicação foi finalizada!!")