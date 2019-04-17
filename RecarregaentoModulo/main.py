


#recarregament de modulo utilizando reload

import importlib
from _ast import mod

import mod_a

del(mod_a.b) # deletando do escopo global a variavel B
mod_a.a = 0 # alterando o valor da variavel A


#função .reload solicita que seja
# passado como parametro um modulo

importlib.reload(mod_a)


from pprint import pprint

pprint(mod.a.__dict__) #manda imprimir todos simbolos contidos no modulo mod_a
