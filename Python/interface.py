# Exemplo 1: janela simples e moderna

import customtkinter as ctk

# Instalar: pip install customtkinter

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("400x300")

texto = ctk.CTkLabel(janela, text="Ola! Interface Moderna!",
                     font=("Arial", 20))
texto.pack(pady=20)

janela.mainloop()