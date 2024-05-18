def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media2aprovacao = float(input("Qual a media para aprovação: "))
media = calcular_media(nota1, nota2, nota3)
print("A média das notas é:", media)
if media>=media2aprovacao:
    print("E o(a) aluno(a) está Aprovado!")
else:
    print("E o(a) aluno(a) está Reprovado!")