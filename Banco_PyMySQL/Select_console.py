#importando o package pymysql para realizar a conexao com o banco de dados mysql

import pymysql.cursors



conexao = pymysql.connect (

    host='localhost',
    user='admin',
    password='Jojo*21021990',
    db='DBI',
    cursorclass = pymysql.cursors.DictCursor

)
#trazendo as informaçẽos da tabela
with conexao.cursor() as cursor:
    cursor.execute('select * from pessoa')
    resultado  = cursor.fetchall()

#printando o resultado e formatando o mesmo
for dado in resultado:
    print('Nome: {}' .format(dado['nome']))
    print('Idade: {}'.format(dado['idade']))
    print('Endereço:{}'.format(dado['endereco']))
    print(' ')