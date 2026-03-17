# 5.6

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("600x400")

titulo = ctk.CTkLabel(janela, text="Lista de Tarefas", font=("Arial", 15))
titulo.pack(pady=5)

