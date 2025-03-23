# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Vamos lá!

# Primeiro, vamos solicitar o primeiro número do usuário

num1 = float(input("Digite o primeiro número: "))

# Agora, vamos solicitar o segundo número do usuário

num2 = float(input("Digite o primeiro número: "))

# Agora, vamos realizar a operação entre os números

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
potencia = num1 ** num2

# Por fim, vamos exibir os resultados das operações
print("Resultados das operações:")
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"Divisão: {num1} / {num2} = {divisao}")
print(f"Potência: {num1} ** {num2} = {potencia}")