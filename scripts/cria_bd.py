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
    # Conectar ao servidor MySQL com SSL
    conexao = mysql.connector.connect(
        user=usuario,
        password=senha,
        host=host,
        port=3306,
        ssl_ca=ssl_ca,
        ssl_verify_cert=True
    )

    cursor = conexao.cursor()

    print("Criando banco de dados ...")

    database = 'azure_company'

    # Criar o banco de dados (se ainda não existir)
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
    cursor.execute(f"USE {database};")

    print(f'Banco de dados {database} criado!!')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro de acesso: Verifique seu usuário e senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(f"Erro: {err}")
        print(f"Mensagem de erro detalhada: {err.msg}")  # Mensagem detalhada
finally:
    # Fechar a conexão se ela foi criada
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão fechada.....")
