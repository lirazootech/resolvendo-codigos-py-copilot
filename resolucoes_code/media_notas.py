# Vamos calcular a média de três notas informadas pelo usuário.

# Vamos lá!

# Primeiro, vamos receber as notas do usuário

nota1 = float(input("Digite a primeira nota, um valor de 0 a 10. Obs: Use o '.' como separador decimal: "))
nota2 = float(input("Digite a segunda nota, um valor de 0 a 10. Obs: Use o '.' como separador decimal: "))
nota3 = float(input("Digite a terceira nota, um valor de 0 a 10. Obs: Use o '.' como separador decimal: "))

# Agora, vamos calcular a média das notas

media = (nota1 + nota2 + nota3) / 3

# Por fim, vamos exibir a média das notas

print("A média das notas é: ", media)

if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação!")
else:
    print("Reprovado!")

# Linha em branco para separar as operações
print()