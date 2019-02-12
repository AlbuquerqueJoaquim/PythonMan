#
#

print()
print("Inicio")

i = 0

while(i<10):
    i += 1
    if (i%2==0):
        continue #volta para a linha 4 se i for divisivel por 2
    if(i>5):
        break # caso i seja maior que 5 utiliza break para parar clausula while
    print(i)
else:
    print("Else")
print("Fim") # será executado após i ser maior que 5
print()
