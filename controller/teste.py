from model import *

usuario='admin'
senha_digitada = 'admin'
resultado = pesquisa_usuario(usuario)
resultado = resultado[3]

# Converte a string recuperada para bytes
resultado_bytes = resultado.encode('utf-8')w

# Função para verificar a senha
def verificar_senha(senha_digitada, senha_banco):
    return bcrypt.checkpw(senha_digitada.encode(), senha_banco)

# Verifica a senha
retorno = verificar_senha(senha_digitada, resultado_bytes)
print("Senha válida:", retorno)