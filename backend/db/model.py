from flask import Flask
import mysql.connector
from hashlib import sha256

app = Flask(__name__)

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'chuckito'
)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar um novo banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS login")

# Conectar ao novo banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="chuckito",
    database="login"
)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar uma tabela
def criar_tabela():
    # Conectar ao novo banco de dados
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="chuckito",
    database="login"
    )

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(120) NOT NULL UNIQUE,
        senha VARCHAR(100) NOT NULL
    )
""")
    # Confirmar as alterações
    conexao.commit()

    # Fechar a conexão
    cursor.close()
    conexao.close()

# Criar uma tabela
def adicionar_na_tabela(usuario):
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'chuckito',
    database="login"
    )
    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()
    senha = usuario.senha
    senha_byte = senha.encode('utf-8')
    crypt = sha256(senha_byte).hexdigest()
    try:
        cursor.execute("""
        INSERT INTO usuario (email, senha) VALUES (%s, %s)
                       """, (usuario.email, crypt))
        # Confirmar as alterações
        conexao.commit()
        
        return True
    except Exception as e:
        print('erro: ', e)
        return (f"Erro ao inserir usuario: {e}")
    finally:
        # Fechar a conexão no bloco finally para garantir que seja fechada, mesmo em caso de exceção
        cursor.close()
        conexao.close()

def recuperar_na_tabela(usuario):
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'chuckito',
    database="login"
    )
    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()
    senha = usuario.senha
    senha_byte = senha.encode('utf-8')
    crypt = sha256(senha_byte).hexdigest()

    try:
        cursor.execute("""
        SELECT email FROM usuario WHERE email = %s AND senha = %s
                       """, (usuario.email, crypt))

        resultados = cursor.fetchone()
        
        return resultados
    except Exception as e:
        print('erro: ', e)
        return (f"Erro ao encontrar usuario: {e}")
    finally:
        # Fechar a conexão no bloco finally para garantir que seja fechada, mesmo em caso de exceção
        cursor.close()
        conexao.close()

def deletar_na_tabela(usuario):
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'chuckito',
    database="login"
    )
    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()
    
    try:
        cursor.execute("""
        DELETE FROM usuario WHERE email = %s
                       """, (usuario.email,))

        # Aplicar a alteração no banco de dados
        resultado = conexao.commit()

        # Verificar se algum registro foi afetado
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print('erro: ', e)
        return (f"Erro ao encontrar usuario: {e}")
    finally:
        # Fechar a conexão no bloco finally para garantir que seja fechada, mesmo em caso de exceção
        cursor.close()
        conexao.close()

criar_tabela()

# Confirmar as alterações
conexao.commit()

# Fechar a conexão
cursor.close()
conexao.close()