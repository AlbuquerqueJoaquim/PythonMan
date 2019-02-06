

#Nesse codigo estaremos trabalhando com escopo,
#mostrando variaveis globais e local

a = 1 # variaveis globais
b = 2 # variaveis globais

def soma_num(var1, var2): # variaveis locais somente serão enchergadas nesta função
    s = var1+var2
    return s

def imprime(x_vezes): # variaveis locais somente serão enchergadas nesta função
    for i in range(x_vezes):
        print(i)
print(soma_num(a,b))
imprime(5)
