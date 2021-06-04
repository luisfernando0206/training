bonus = int(input("Digite a pontuação: "))

if bonus > 1000:
    print("Você ganhou 3gb de bônus")
elif bonus > 500:
        print("Você ganhou 1,5gb de bônus")
elif bonus > 200:
    print("Você ganhou 500mb de bônus")
else:
    print("Você não ganhou nada")
