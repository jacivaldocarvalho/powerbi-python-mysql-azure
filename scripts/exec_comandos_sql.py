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
ssl_ca = config['mysql']['ssl_ca']  # certificado CA


try:
    # Conectar ao servidor MySQL
    conexao = mysql.connector.connect(
        user=usuario,
        password=senha,
        host=host,
        port=3306,  # Porta do MySQL
        ssl_ca=ssl_ca,  # Caminho para o arquivo CA
        ssl_verify_cert=True  # Verifica o certificado SS
    )

    cursor = conexao.cursor()

    database = 'azure_company'

    # Seta o banco de dados azure_company
    print(f'Seleciona o banco de dados {database} ...\n')
    cursor.execute(f"USE {database};")

    print("Executando o comando SQL ...\n")

    # Executar comandos SQL
    cursor.execute(
        """
        select *from works_on;
           
        """
    )

    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)     

    print("\nTabela/Alteração/Inserção realizada com sucesso!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro de acesso: Verifique seu usuário e senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(err)
finally:
    # Fechar o cursor e a conexão
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()
