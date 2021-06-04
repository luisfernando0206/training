nome_completo = input("Digite seu nome completo: ")
print("Seu nome é {}" .format(nome_completo))

#variavel_float = 5.2
#print(variavel_float)
#variavel_int = int(variavel_float)
#print(variavel_int)

nome_funcionario = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario < 0:
    salario = salario * -1
    print("O salário é negativo")

print("O salário do funcionário é: {}".format(salario))

idade = int(input("Digite sua idade"))
nome = input("Digite o seu nome: ")