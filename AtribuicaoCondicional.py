
#Atribuição condicional verificando se número e par ou impar
num1 = int(input("Digite um numero: "))

if(num1 % 2 == 0):
    s = "par"
else:
    s = "impar"

print("O número digiado é ", s)