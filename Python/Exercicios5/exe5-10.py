# 5.10

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("600x400")

titulo = ctk.CTkLabel(janela, text="Formulario de Cadastro", font=("Arial", 15))
titulo.pack(pady=5)

entrada1 = ctk.CTkEntry(janela, placeholder_text=("Nome: "))
entrada1.pack(pady=5)

entrada2 = ctk.CTkEntry(janela, placeholder_text=("Email: "))
entrada2.pack(pady=5)

entrada3 = ctk.CTkEntry(janela, placeholder_text=("Idade: "))
entrada3.pack(pady=5)


saida = ctk.CTkLabel(janela, text="", font=("Arial", 10))
saida.pack(pady=5)







janela.mainloop()