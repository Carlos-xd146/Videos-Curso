# 5.6

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("600x400")

titulo = ctk.CTkLabel(janela, text="Lista de Tarefas", font=("Arial", 15))
titulo.pack(pady=5)

def adicionar_tarefa():
    texto = entrada.get()
    tarefa = ctk.CTkLabel(scroll, text=texto, width=200, height=40)
    tarefa.pack(pady=1)

frame1 = ctk.CTkFrame(janela, height=40)
frame1.pack(pady=5,side="top",fill='x')

entrada = ctk.CTkEntry(frame1, placeholder_text="tarefa", width=200, height=40)
entrada.pack(padx=20, side='left')

botao = ctk.CTkButton(frame1, text='+', command=adicionar_tarefa, width=40, height=40)
botao.pack(padx=50,side="right")

scroll = ctk.CTkScrollableFrame(janela)
scroll.pack(side='bottom', fill='y')

janela.mainloop()
