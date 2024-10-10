import configparser
import mysql.connector
from mysql.connector import errorcode

# Ler configurações do arquivo config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Obter as credenciais do MySQL
usuario = config['mysql']['user']
senha = config['mysql']['password']
host = config['mysql']['host']
ssl_ca = config['mysql']['ssl_ca']  # Caminho para o certificado CA

try:
    # Conectar ao servidor MySQL sem especificar o banco de dados
    conexao = mysql.connector.connect(
        user=usuario,
        password=senha,
        host=host,
        port=3306,
        ssl_ca=ssl_ca,
        ssl_verify_cert=True
    )

    print("Conexão SSL bem-sucedida!")

    cursor = conexao.cursor()

    # Mostrar todos os bancos de dados
    cursor.execute("SHOW DATABASES;")
    bancos_de_dados = cursor.fetchall()

    print("Bancos de dados disponíveis:")
    for db in bancos_de_dados:
        print(db[0])  # Imprime o nome do banco de dados

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro de acesso: Verifique seu usuário e senha")
    else:
        print(f"Erro: {err}")
finally:
    # Fechar a conexão se ela foi criada
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão fechada.")
