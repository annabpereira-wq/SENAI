contador = 1
soma_notas = 0

while contador <=4:
    nota =float(input(f"digite a nota do {contador} bimestre"))
    contador += 1
    if notas < or notas > 10:
        print+("nota invalida. A nota deve estar entre 0 e 10")
        continue
    contador += 1
    soma_notas += nota
media = soma_notas / 4
print("a media de notas é: ", media)

if media >= 7:
        print("o aluno esta aprovado")
if media >=  5:
        print("o aluno esta em pecuperação")
else:
        print("o aluno esta reprovado")


