import customtkinter as ctk

def saudar():
    nome = entrada.get()
    resposta =  "Olá, "+nome
    texto.configure(text=resposta)
    

janela = ctk.CTk()
janela.geometry("400x200")

entrada = ctk.CTkEntry(janela, placeholder_text="Seu Nome", width=200, height=40)
entrada.pack(pady=20)

botao = ctk.CTkButton(janela, text="Saudar!", command=saudar)
botao.pack(pady=10)

texto = ctk.CTkLabel(janela, text="", width=200, height=40)
texto.pack(pady=10)

janela.mainloop()