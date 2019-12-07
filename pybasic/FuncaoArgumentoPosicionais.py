#cofing: utf-8


#Passando argumentos posiionais e argumentos nomeados em uma função

def dados_pessoais(nome, sobreme, idade, sexo):# passando parametros
    print("Nome: {} \nSobrenome:{} \nIdade:{} \nSexo:{}"
          .format(nome,sobreme,idade,sexo))

#dados_pessoais("Jose","Silva","30","True") passando parametros fixos ou possivionais
dados_pessoais(idade=30, sexo=True, sobreme="Silva",nome="Jose")# passando argumentos nomeados e fora de ordem