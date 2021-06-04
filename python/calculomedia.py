notas = []
aluno = [""]

aluno.append(input("Digite o nome do aluno que deseja calcular a média: "))
notas.append(float(input("Digite uma nota do aluno: ")))

while len(notas) < 4:
    notas.append(float(input("Digite mais uma nota do aluno: ")))
    if len(notas) == 4:
        media = sum(notas) / 4
        print("A media do aluno {} é {}".format(aluno[0], media))