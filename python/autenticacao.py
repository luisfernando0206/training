import hashlib

#Criando uma lista vazia chamada “usuários”
usuarios = []

#Criando um usuário como dicionário com name, username e password
usuario = {
    "name": "Clark Kent",
    "username" : "kent",
    "password" : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2" 
}
# Inclui este usuário na lista usuários
usuarios.append(usuario)

#Criando um usuário como dicionário com name, username e password
usuario = {
    "name": "Bruce Wayne",
    "username" : "wayne",
    "password" : "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a" 
}
# Inclui este usuário na lista usuários
usuarios.append(usuario)

#Criando um usuário como dicionário com name, username e password
usuario = {
    "name": "Christopher Walker",
    "username" : "walker",
    "password" : "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83" 
}


# Inclui este usuário na lista usuários
usuarios.append(usuario)

#recebe o input do usuário
autentica_usuario = input("Digite o usuário em letras minúsculas: ")
#recebe o input da senha
converte_senha = input("Digite a senha: ")
#converte a senha digitada para bytes e codifica em utf-8
converte_senha = bytes(converte_senha, 'utf-8')
#converte a senha para hash no formato sha-256 dentro de uma lista
autentica_senha = ("SHAP-256:", hashlib.sha256(converte_senha).hexdigest())
#cria a variável usuario_login no formato inteiro que será usada no loop for
usuario_login = 0
#Cria a variável result como tipo boolean como uma forma de escape do loop para caso o loop for false
result = False
#inicia o loop for buscando o valor de usuario_login na lista usuarios
for usuario_login in usuarios:
    #testa se a variavel autentica_usuario e autentica_senha informada pelo usuario existe dentro do dicionário, usando a key username e password
    if autentica_usuario == usuario_login["username"] and autentica_senha[1] == usuario_login["password"]:
        #printa para o usuário que ele conseguiu autenticar
        print("O usuário {} está logado com sucesso".format(usuario_login["name"]))
        #ajusta o valor do result para true porque a condição foi verdadeira
        result = True
        #para o loop for
        break
#condicao para o usuario caso o usuário ou senha forem falsos
if result == False:
    print("Usuário ou senha inválidos")
    

    