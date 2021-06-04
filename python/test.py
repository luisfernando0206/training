#importação do módulo calc.py
import calc
#importação de funções específica do módulo calc.py
#---- from calc import somar, subtrair
#importação de todas funções do módulo calc.py, cuidar pois pode deixar o sistema lento
#---- from calc import *
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = calc.somar(valor1, valor2)
#chamando a funcao sem o nome do módulo
# ------ soma = somar(valor1, valor2)
#exibindo a soma
print("A soma é {}".format(soma))