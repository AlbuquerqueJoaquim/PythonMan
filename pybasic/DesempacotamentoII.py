# coding: utf-8

#


lista = [11,20,30,]
tupla = [1,2,3]


def func(a,b,c):
    print(a)
    print(b)
    print(c)

lista.sort() # ordenando a funcao utirlizando o sort
func(*lista) # desempacotamento da lista com a função func

l = [*tupla] #convertendo o elemento do tipo tupla par o tipo lista e assosiando a variavel L
l.sort() # ordenando os elementos
func(*l)

func(**dict(zip(("a","b","c"), lista)))