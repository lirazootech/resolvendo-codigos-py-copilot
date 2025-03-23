#Vamos solicitar uma string e um número inteiro como entrada. Em seguida, teremos que retornar a string na quantidade de vezes informada pelo número inteiro.

# Vamos lá!

# Primeiro, vamos receber a string do usuário

texto = input("Digite uma string: ")

# Agora, vamos receber a quantidade de vezes que a string deve ser repetida

quantidade = int(input("Digite a quantidade de vezes que a string deve ser repetida: "))

# Agora, Vamos repetir a string

resultado = " ".join([texto] * quantidade)

# Por fim, vamos exibir o resultado da repetição

print("O resultado da repetição é: ", resultado)





