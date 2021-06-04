import requests

#Atribui a variável url o endereço do webservice
url_api = 'https://dc1-2021.glitch.me/getHash'

#Variável user_data recebe o valor para ser realizado o envio
send_data = {
    "rm": 86693,
    "senha":'7FcmhuknTB'
}

#Atribui a variável resposta a lib de post com os dados necessários para o envio
resposta = requests.post(url=url_api, json=send_data)

#Printa a resposta do conteúdo JSON (SEMPRE SERÁ 200 SE ENVIADO COM DADOS INVÁLIDOS)
if resposta.status_code >= 200 and resposta.status_code <= 299:
    #Sucesso
    print("Status code: ", resposta.status_code)
    print("Reason: ", resposta.reason)
    print("Resposta: ", resposta.json())
else:
    #Falhou a requisição
    print("Status code: ", resposta.status_code)
    print("Reason: ", resposta.reason)
    print("Resposta: ", resposta.json())