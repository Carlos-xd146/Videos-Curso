# 5.3

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Exercicio 3")
janela.geometry("400x400")


titulo1 = ctk.CTkLabel(janela, text="Temperatura", font=("Arial", 20))
titulo1.pack(pady=0.5)

entrada = ctk.CTkEntry(janela, placeholder_text="Temperatura C°: ", width=200, height=40)
entrada.pack(pady=3)


def conversao():
    
    temperatura = float(entrada.get())

    fahrenheit = (temperatura*1.8)+32

    saida1.configure(text= fahrenheit)
  


botao = ctk.CTkButton(janela, text="Calcular", command=conversao)
botao.pack(pady=20)

saida1 = ctk.CTkLabel(janela, text="",
                      font=("Arial", 20))
saida1.pack(pady=10)


janela.mainloop()
