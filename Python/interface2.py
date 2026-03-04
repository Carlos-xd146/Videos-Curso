# Exemplo 2: botao moderno com açao

import customtkinter as ctk

def clicar():
    print("Botão clicado")

janela = ctk.CTk()
janela.geometry("400x300")

botao = ctk.CTkButton(janela, text="Clique Aqui",
                      command=clicar,
                      width=200, height=40,
                      fg_color="Red")
botao.pack(pady=50)

janela.mainloop()
