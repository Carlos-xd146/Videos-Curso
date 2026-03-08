# 4.1

# nome = input("Nome: ")
# periodo = float(input("Periodo: "))

# def saudar(nome, periodo):
#     if periodo >=0 and periodo <= 12:
#         periodo = "Bom dia"
#     elif periodo >=13 and periodo <= 18:
#         periodo = "Boa tarde"
#     else:
#         periodo = "Boa noite"

#     mensagem = f"{periodo}, {nome}!"
#     return mensagem

# resultado = saudar(nome, periodo)
# print(resultado)

# 4.2

# num1 = int(input("Numero 1: "))
# num2 = int(input("Numero 2: "))
# operacao = input("Operacao: ")

# def calcular(num1, num2, operacao):
#     if operacao == "+":
#         print(num1+num2)
#     elif operacao == "-":
#         print(num1-num2)
#     elif operacao == "*":
#         print(num1*num2)
#     elif operacao == "/":
#         print(num1/num2)

# resultado = calcular(num1, num2, operacao)
# print(resultado)

# 4.3 

# def validar_email(email):
#     tem_ponto = False
#     tem_arroba = False

#     for letra in email:
#         # debug
#         print("Letra atual:",letra)
#         print("Valido ponto:", letra == '.')
#         print("Valido @:", letra == '@')
#         print(" ")
#         if letra == '.':
#             tem_ponto = True

#         if letra == '@':
#             tem_arroba= True

#     if tem_arroba and tem_ponto:
#         return True
#     else:
#         return False

# entrada = input("Email: ") # fabio@gmail.com

# resposta = validar_email(entrada)
# print("Resposta: ", resposta)



# 4.4

# temperatura = int(input("Celsius: "))

# def conversao(celsius):
#     fahrenheit = (celsius*1.8)+32
#     return fahrenheit

# resultado = conversao(temperatura)
# print(resultado)

# 4.5

# circulo = int(input("Raio de Circulo: "))

# def calculoArea(raio):
#     area = 3.14159 * (raio*raio)
#     return area

# resultado = calculoArea(circulo)
# print(resultado)

# 4.6

# verificacao = int(input("Idade: "))

# def pode_dirigir(idade):
#     if idade >= 18:
#         print("Pode dirigir")
#     else:
#         print("Não pode dirigir")

# resultado = pode_dirigir(verificacao)
# print(resultado)

# 4.7



# 4.8

# preco = int(input("Preço: "))
# desconto = int(input("Desconto: "))

# def aplicar_desconto(preco, desconto):
#     resultado = preco - ((desconto/100)*preco)
#     return resultado

# resposta = aplicar_desconto(preco, desconto)
# print(resposta)

# 4.9

# base = int(input("Base: "))
# expoente = int(input("Expoente: "))

# def potencia(base, expoente):
#     resultado = 1
#     for i in range(expoente):
#         resultado = resultado * base
#     return resultado

# resposta = potencia(base, expoente)
# print(resposta)

# 4.10