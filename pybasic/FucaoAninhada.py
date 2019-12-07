#coding: utf-8



#funcoes aninhadas e uma funçao dentro de outra funcão

def func():

    print( "func")

    def func_interna():
        print("func_interna")

    func_interna()

func()