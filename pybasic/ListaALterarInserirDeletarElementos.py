
#Alterar inserir e deletando itens de uma lista

lista = ['aaa','bbb','ccc','ddd','eee']

deletar = lista.pop(-1)
del(lista[::2])
lista.insert(0,'zzz') # inserindo eletemento na posiçao
                      # inicial tbem pode se usar para alterar elementos


#list.clear() delete a lista toda

print(deletar)
print(lista)