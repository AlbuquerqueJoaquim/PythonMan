#coding: utf-8


def lista_de_argumentos(*args):#args recebe varios argumentos
    print(args)

def lista_de_argumentos_associativos(**kwargs):# kwargs tipo dicionairo sempre com chave e a string
    print(kwargs)

def argumentos(*args, **kwargs):# utilizando os dois
    print(args)
    print(kwargs)

argumentos(1,2,3,5, um=1,doois=2,quatro=4)

lista_de_argumentos(1,2,3,4,5,6,7)
lista_de_argumentos("zero","um","dois","quatro","cinco")

lista_de_argumentos_associativos(a=1,b=2,c=3,d=4)
lista_de_argumentos_associativos(um=1,dois=2,cinco=5,seis=6,sete=7)