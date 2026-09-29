# Sistema de Média do Aluno - Versão Final

print("--- Sistema de Média do Aluno ---")

# Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Processamento
media = (nota1 + nota2 + nota3) / 3


print(f"\nAluno: {nome}")
print(f"A média do aluno foi de: {media:.2f}")

#Saída de dados
if media >= 7.0:
    print("Status: Aluno APROVADO! 🎉")
elif media >= 5.0:
    print("Status: Aluno em RECUPERAÇÃO! ⚠️")
else:
    print("Status: Aluno REPROVADO! ❌")