# ----- 1.1 - variaveis

# peso = float(input("Peso: "))
# altura = float(input("altura: "))

# saida = peso/(altura**2)

# print("IMC: ",saida)

# ----- 2.10 if

# usuario = input("Usuario: ")
# senha = input("Senha: ")

# if usuario=="admin" and senha=="1234":
#     print("login bem-sucedido")
# else:
#     print("login falhou")

# ----- for
# exemplo 1
# for i in range(1, 6):
#     print("Número:", i)

# exemplo 2

# for i in range(1, 11):
#     resultado = 5 * i
#     print(f"5 x {i} = {resultado}")

# exemplo 3

# resposta = 0
# numero = int(input("Número: "))

# for i in range(1, numero):
#     resposta = resposta + i
#     print(f"Resultado: {resposta-i} + {i} = {resposta}")

# # piramide 

num = int(input("Numero: "))
for i in range(1,num):
    print("O"*i)

# ----- exercicio 3 - FOR



# exemplo 1: função

# def saudar(nome):
#     mensagem = f"Olá, {nome}!"
#     return mensagem

# resultado = saudar("Ana")
# print(resultado)

# Exemplo 2 : calculadora simples

# def somar(a, b):
#     return a + b

# resultado = somar(10, 5)
# print("Resultado: ", resultado)

# desafio:

# num1 = int(input("Numero1: "))
# num2 = int(input("Numero2: "))

# def div (a,b): 
#     return (a + b) / 2

# resultado = div(num1, num2)
# print(resultado)    
