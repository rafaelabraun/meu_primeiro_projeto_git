# Sistema de Média do Aluno - Versão 2.0
print("--- Sistema de Média do Aluno ---")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("A média do aluno foi de: ", media)
if media >= 7.0:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")