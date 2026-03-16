# 5.5

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("400x300")

titulo = ctk.CTkLabel(janela, text="Gerador de Saudações", font=("Arial", 20))
titulo.pack(pady=10)


saida = ctk.CTkLabel(janela, text="", font=("Arial", 20))
saida.pack(pady=20)


def saudacao(msg):
    saida.configure(text=msg)

botao1 = ctk.CTkButton(janela, text="Bom dia", command=lambda: saudacao("Bom dia"))
botao1.pack(pady=5)

botao2 = ctk.CTkButton(janela, text="Boa tarde", command=lambda: saudacao("Boa tarde"))
botao2.pack(pady=5)

botao3 = ctk.CTkButton(janela, text="Boa noite", command=lambda: saudacao("Boa noite"))
botao3.pack(pady=5)

janela.mainloop()

