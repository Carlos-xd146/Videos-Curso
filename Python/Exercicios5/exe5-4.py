# 5.4

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("400x300")

titulo = ctk.CTkLabel(janela, text="Calculadora + e -", font=("Arial", 20))
titulo.pack(pady=3)

num = ctk.CTkLabel(janela, text="0", font=("Arial", 20))
num.pack(pady=3)

numero = 0

def soma():
    global numero
    numero = numero + 1
    num.configure(text=numero)

def subtracao():
    global numero
    numero = numero - 1
    num.configure(text=numero)

    
botao1 = ctk.CTkButton(janela, text="+", command=soma)
botao1.pack(pady=5)

botao2 = ctk.CTkButton(janela, text="-", command=subtracao)
botao2.pack(pady=5)

janela.mainloop()