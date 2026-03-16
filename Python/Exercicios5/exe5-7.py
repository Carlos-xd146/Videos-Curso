# 5.7

import customtkinter as ctk

janela = ctk.CTk()
janela.title("Minha Janela")
janela.geometry("600x400")

titulo = ctk.CTkLabel(janela, text="Calculadora Simples", font=("Arial", 20))
titulo.pack(pady=30)


entrada1 = ctk.CTkEntry(janela, placeholder_text="Numero: ", width=200, height=40)
entrada1.pack(pady=10)

entrada2 = ctk.CTkEntry(janela, placeholder_text="Numero: ", width=200, height=40)
entrada2.pack(pady=10)

saida = ctk.CTkLabel(janela, text="", font=("Arial", 20))
saida.pack(pady=10)


def calculo(cal):
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())

    if cal == "+":
        resultado = num1 + num2
    elif cal == "-":
        resultado = num1 - num2
    elif cal == "x":
        resultado = num1 * num2
    elif cal == "÷":
        resultado = num1 / num2
    
    saida.configure(text=resultado)

botao1 = ctk.CTkButton(janela, text="+", command=lambda: calculo("+"))
botao1.pack(side="left", padx=5)

botao2 = ctk.CTkButton(janela, text="-", command=lambda: calculo("-"))
botao2.pack(side="left", padx=5)

botao3 = ctk.CTkButton(janela, text="x", command=lambda: calculo("x"))
botao3.pack(side="left", padx=5)

botao4 = ctk.CTkButton(janela, text="÷", command=lambda: calculo("÷"))
botao4.pack(side="left", padx=5)


janela.mainloop()