def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    return velocidade_media

#solicitar distância e tempo
distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite o tempo da viagem: "))

print("A velocidade média é {} km/h".format(calcularVelocidadeMedia(distancia, tempo)))