#Utilizando enumerate em uma lista

lista_nums = [100,200,300,400]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)