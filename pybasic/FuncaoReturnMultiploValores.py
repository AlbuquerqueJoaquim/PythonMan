
#coding:utf-8


def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo

q,c = potencia(10)#q e c estão recebendo quadrado e cubo como return da funcao

print(q)
print(c)