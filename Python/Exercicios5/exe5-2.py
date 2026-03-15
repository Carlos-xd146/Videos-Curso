# 5.2

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Minha Janela")
# janela.iconbitmap("./imc.ico")
janela.geometry("400x400")

titulo1 = ctk.CTkLabel(janela, text="Peso", font=("Arial", 20))
titulo1.pack(pady=0.5)
entrada1 = ctk.CTkEntry(janela, placeholder_text="Seu Peso: ", width=200, height=40)
entrada1.pack(pady=3)

espaco = ctk.CTkLabel(janela, text=" ", font=("Arial", 20))
espaco.pack(pady=6)

titulo2 = ctk.CTkLabel(janela, text="Altura", font=("Arial", 20))
titulo2.pack(pady=0.5)
entrada2 = ctk.CTkEntry(janela, placeholder_text="Sua Altura: ", width=200, height=40)
entrada2.pack(pady=3)


saida1 = ctk.CTkLabel(janela, text="",
                      font=("Arial", 20))
saida1.pack(pady=10)
saida2 = ctk.CTkLabel(janela, text="",
                      font=("Arial", 20))
saida2.pack(pady=10)

def calculo():
    peso = float(entrada1.get())
    altura = float(entrada2.get())
    resposta = ""

    imc = peso/(altura**2)


    if imc<18.5:
        resposta = "Abaixo do peso"
    elif imc>=18.5 and imc<=24.9:
        resposta = ("Peso normal")
    elif imc>=25 and imc<=29.9:
        resposta = ("Sobrepeso")
    else:
        resposta = ("Obesidade")

    saida1.configure(text= resposta)
    saida2.configure(text= imc)

botao = ctk.CTkButton(janela, text="Calculo IMC", command=calculo)
botao.pack(pady=20)


janela.mainloop()

