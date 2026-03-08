# 5.1

# import customtkinter as ctk

# janela = ctk.CTk()
# janela.title("Minha Janela")
# janela.geometry("400x300")

# titulo = ctk.CTkLabel(janela, text="Bem-vindo!",
#                      font=("Arial", 30))
# titulo.pack(pady=20)

# texto = ctk.CTkLabel(janela, text="Olá, seja bem-vindo ao Python!",
#                      font=("Arial", 15))
# texto.pack(pady=20)

# def fechar():
#     janela.destroy()

# botao = ctk.CTkButton(janela, text="Fechar", command=fechar)
# botao.pack(pady=20)

# janela.mainloop()


# 5.2

# import customtkinter as ctk

# janela = ctk.CTk()
# janela.title("Minha Janela")
# janela.geometry("400x300")

# entrada1 = ctk.CTkEntry(janela, placeholder_text="Seu Peso: ", width=200, height=40)
# entrada1.pack(pady=20)

# entrada2 = ctk.CTkEntry(janela, placeholder_text="Sua Altura: ", width=200, height=40)
# entrada2.pack(pady=20)

# def calculo():
#     peso = entrada1.get()
#     altura = entrada2.get()

#     IMC = peso/(altura**2)

#     if IMC<18.5:
#         print("Abaixo do peso")
#     elif IMC>=18.5 and IMC<=24.9:
#         print("Peso normal")
#     elif IMC>=25 and IMC<=29.9:
#         print("Sobrepeso")
#     else:
#         print("Obesidade")



# botao = ctk.CTkButton(janela, text="Calculo IMC", command=calculo)
# botao.pack(pady=20)

# janela.mainloop()

