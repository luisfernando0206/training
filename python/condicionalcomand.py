valor_compra = float(input("Digite o valor da compra: "))
forma_pagamento = int(input("1 - Dinheiro / 2 - Cartão: "))

if valor_compra > 100 and forma_pagamento==1:
    print("Você tem direiro a um desconto")
