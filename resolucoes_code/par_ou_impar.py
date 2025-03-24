# Vamos receber como entrada um número inteiro para saber se ele é par, ímpar ou neutro.

# Vamos lá!

num1 = int(input("Digite o número inteiro para saber se ele é par ou ímpar: "))

# Condição para definir se o número é par ou ímpar

if num1 == 0:
    print("O número 0 é neutro.")
elif num1 % 2 == 0:
    print(f"O número {num1} é par.")   
else:
    print(f"O número {num1} é ímpar.")

# Linha em branco para separar as operações

print() 