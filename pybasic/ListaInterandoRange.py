#Utilizando range para listar uma lista

lista_nums = [100,200,300,400,500,600]
for item in range(len(lista_nums)):# utilizando len para carregar os números que forem add na lista
    lista_nums[item] +=1000
print(lista_nums)