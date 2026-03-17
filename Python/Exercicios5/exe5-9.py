import customtkinter as ctk
import random

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("600x400")

titulo = ctk.CTkLabel(janela, text="Gerador de Senha", font=("Arial", 15))
titulo.pack(pady=5)

def gerarSenha():
    letras_numeros = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    senha = ''

    for numero in range(8):
        senha = senha + letras_numeros[random.randrange] 