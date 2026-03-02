# 3.1

# num = 10

# for i in range(0, 10):
#     resposta = num - i
    
#     print(f"{resposta}")
# print(f"FIM!")


# 3.2

# numero = int(input("Número: "))

# for i in range(1, numero):
#     resposta = numero * i
#     print(f"Resultado: {numero}*{i} = {resposta}")

# 3.3

# resposta = 0 
# num = int(input("Numero: "))

# for i in range(1, num+1):
#     resposta = resposta + i
# print(resposta)

# 3.4

# for i in range (1, 52):
#     if (i % 2)-1:
#         print(i) 

# 3.5
# total_par = 0
# total_impar = 0
# total_positivo = 0
# total_negativo = 0


# for i in range (1, 6):
#     numero_x = int(input(f"Numero {i}: "))
#     if numero_x <0:
#         total_negativo = total_negativo+1
#     if numero_x >0:
#         total_positivo = total_positivo+1
#     if numero_x % 2 == 0:
#         total_par = total_par+1
#     else:
#         total_impar = total_impar+1
    
#     primo = True
#     for i in range(2, numero_x):
#         print(numero_x,"%", i,"=",numero_x%i)
#         if numero_x%i == 0:
#             primo = False
#             break
    
    

        
# print("Existe", total_negativo, "números negativos.")    
# print("Existe", total_positivo, "números positivos.")
# print("Existe", total_par, "números pares.")
# print("Existe", total_impar, "números inpares.")

# 3.6
# resultado = 0

# for i in range (1, 6):
#     nota = int(input(f"Nota {i}: "))
#     resultado = resultado + nota

# resposta = resultado / 5

# print(resposta)
    
# 3.7

# maior = 0
# for i in range(1, 6):
#     num = int(input(f"numero {i}: "))
#     if num > maior:
#         maior = num
# print(f"{maior} é maior")
        
# 3.8

# resposta = 1
# num = int(input("Numero: "))

# for i in range (1, num+1):
#     resposta = resposta*i

# print(resposta)

# 3.9

# num = int(input("Numero: "))

# for i in range (num):
#     print("*" * num)


# 3.10

# numero = int(input("Insira o numero: "))
# primo = True
# for i in range(2, numero):
#     print(numero,"%", i,"=",numero%i)
#     if numero%i == 0:
#         primo = False
#         break

# if primo: 
#     print(numero,"é Primo")
# else:
#     print(numero,"não é primo")

