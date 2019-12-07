

#Escglobals()opo global


num = 10;
print(num)

def func():
    global num # acessando a variavel a nivel global
    num = 20
    print(num)

func()

print(num)