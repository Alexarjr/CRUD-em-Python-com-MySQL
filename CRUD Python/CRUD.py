import mysql.connector
import config

def conectar():
    return mysql.connector.connect(
        host="config.HOST",
        user="config.USER",
        password="config.PASSWORD",
        database="config.DATABASE"
    )
    
def criar_usuario(nome, email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    for usuario in cursor.fetchall():
        print(usuario)
    conexao.close()

def atualizar_usuario(id, novo_nome, novo_email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET nome = %s, email = %s WHERE id = %s", (novo_nome, novo_email, id))
    conexao.commit()
    conexao.close()

def excluir_usuario(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()