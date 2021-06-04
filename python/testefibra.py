velocidade_almejada = int(input("Digite um valor de 0 a 100 sobre sua velocidade de internet almejada: "))
print("Os tipos de conexões são 1 - Fibra / 2 - coaxial / 3 - Cabo de rede")
tipo_conexao = int(input("Digite o tipo de conexão:"))

if velocidade_almejada >= 50 and tipo_conexao == 1:
    print("Sua velocidade de conexão é de fibra e muito rápida" )
elif velocidade_almejada >= 50 and tipo_conexao == 2:
    print("Sua velocidade de conexão é de Coaxial e não é tão rápida" )
elif velocidade_almejada > 50 and tipo_conexao == 2:
    print("Sua velocidade de conexão é de Coaxial e é lenta" )
elif velocidade_almejada >= 50 and tipo_conexao == 1:
        print("Sua velocidade de conexão é de cabo normal e rápida" )
    