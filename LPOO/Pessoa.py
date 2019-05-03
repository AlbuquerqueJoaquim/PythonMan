
#trabalhando com classe primeira classe em python
class Pessoa:
    pass

p1 = Pessoa() # realizado a instancia da classe Pessoa na variavel p1
p = p1
p2 = Pessoa()

print(id(p1)) # imprimindo na saida o id do objeto p1
print(id(p2))