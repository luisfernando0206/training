#criação de uma lista com os nome dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#print(jedi[2])

#Acrescenta um valor no final da lista 
jedi.append(input("Digite o nome de um jedi: "))
jedi.insert(0, "Luminara")
#Insere um valor na lista na posição especificada
jedi.insert(6, input("Digite o nome de outro Jedi: "))
#Remove o último valor inserido na lista
jedi.pop()
#Remove o valor da liste com base na sequência do indice
jedi.pop(0)
#Remove um valor especifico independente da posicição
jedi.remove("Darth Vader")

for nome in jedi:
    print(nome)