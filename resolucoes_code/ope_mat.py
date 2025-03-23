# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Vamos lá!

while True:

# Primeiro, vamos solicitar o primeiro número do usuário

    num1 = float(input("Digite o primeiro número: "))

# Agora, vamos solicitar o segundo número do usuário

    num2 = float(input("Digite o primeiro número: "))

# Vamos perguntar ao usuário qual operação ele deseja realizar

    operacao = input("Qual operação você deseja realizar (+, -, *, /, ^, todas)?. Ou digite 'sair' para encerrar: ")

# Verifica se o usuário deseja encerrar o programa

    if operacao.lower() == "sair":
        print("Encerrando o programa. Até mais!")
    break

# Agora, vamos realizar a operação solicitada

if operacao == "+":
    print(f"Resultado da soma: {num1} + {num2} = {num1 + num2}")

elif operacao == "-":
    print(f"Resultado da subtração: {num1} - {num2} = {num1 - num2}")

elif operacao == "*":
    print(f"Resultado da multiplicação: {num1} * {num2} = {num1 * num2}")

elif operacao == "/":
    if num2 == 0:
        print("Não é possível dividir por zero!")
    else:
        print(f"Resultado da divisão: {num1} / {num2} = {num1 / num2}")

elif operacao == "^":
    print(f"Resultado da potenciação: {num1} ** {num2} = {num1 ** num2}")

elif operacao.lower() == "todas":
    print("Resultados das operações:")
    print(f"Soma: {num1} + {num2} = {num1 + num2}")
    print(f"Subtração: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplicação: {num1} * {num2} = {num1 * num2}")
    
    if num2 != 0:     
        print(f"Divisão: {num1} / {num2} = {num1 / num2}")
    else:
        print("Não é possível dividir por zero!")

    print(f"Potência: {num1} ** {num2} = {num1 ** num2}")
else:
    print("Operação inválida. Tente novamente!")

# Linha em branco para separar as operações
print()