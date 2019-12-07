
#Trabalhando com dicionario na pratica


tel = {30300000 : "Manuela",
       33099092: "Paula",
       34568909: "Maisa"}

d = len(tel)
del(tel[30300000]) #deletando item de dentro do dicionario

tel.keys() #aparece apenas as chaves do dicionario
tel.values(33099092)#mostra apenas o valor que for passado como parametro a chave
tel.get(33099092) #mostrar o valor aonde passado parametro utilizando GET
print(tel)