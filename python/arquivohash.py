import hashlib

#f = open("/etc/passwd", "r")

#arquivo = f.read()

#Passar apenas os 4 primeiros caracteres do arquivo /etc/passwd 

hashvalue = 'root'

#Criptografa usando HASH SHA256

hashobj1 = bytes(hashvalue, 'utf-8')

#converte a senha para hash no formato sha-256 dentro de uma lista
printa_obj1 = ("SHAP-256:", hashlib.sha256(hashobj1).hexdigest())

print(printa_obj1)