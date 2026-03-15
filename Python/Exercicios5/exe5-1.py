# 5.1

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("400x300")

titulo = ctk.CTkLabel(janela, text="Bem-vindo!",
                     font=("Arial", 30))
titulo.pack(pady=20)

texto = ctk.CTkLabel(janela, text="Olá, seja bem-vindo ao Python!",
                     font=("Arial", 15))
texto.pack(pady=20)

def fechar():
    janela.destroy()

botao = ctk.CTkButton(janela, text="Fechar", command=fechar)
botao.pack(pady=20)

janela.mainloop()
