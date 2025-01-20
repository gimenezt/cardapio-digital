import sqlite3
import bcrypt

path_tring = r'.\model\db.db'

def pesquisa_usuario(usuario):
    conn = sqlite3.connect(path_tring)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM Funcionarios WHERE Usuario = {usuario}")
    conn.close()
    return cursor.fetchone()