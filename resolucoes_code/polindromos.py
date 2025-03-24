# Vamos testar se uma palavra é um palíndromo.

# Vamos lá!

# Primeiro, vamos receber a palavra do usuário e transformá-la em minúscula

palavra = input("Digite uma palavra para verificar se é um palíndromo: ").lower()

# Agora, vamos verificar se a palavra é um palíndromo

if palavra == palavra[::-1]:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo!")

# Linha em branco para separar as operações

print()