#importando o package pymysql para realizar a conexao com o banco de dados mysql

import  pymysql.cursors



conexao = pymysql.connect (

    host='localhost',
    user='admin',
    password='*******',
    db='DBI',
    cursorclass = pymysql.cursors.DictCursor

)
# pegando as informações
x = input('Digite seu nome : ')
y = input('Digite sua idade : ')
z = input('Digite seu endereço : ')

# executano o SQL
with conexao.cursor() as cursor:
    cursor.execute('insert into pessoa (nome,idade,endereco) values("{}","{}","{}")'.format(x,y,z))
    conexao.commit()
