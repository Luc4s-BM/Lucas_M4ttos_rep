import tkinter as tk

# Função para abrir uma nova janela
def abrir_nova_janela():
    nova_janela = tk.Toplevel()  # Cria uma nova janela secundária
    nova_janela.title("Nova Janela")
    nova_janela.geometry("300x200")  # Define o tamanho da janela
    
    # Adiciona um rótulo na nova janela
    label = tk.Label(nova_janela, text="Esta é uma nova janela!")
    label.pack(pady=20)

# Criação da janela principal
janela_principal = tk.Tk()
janela_principal.title("Janela Principal")
janela_principal.geometry("400x300")

# Botão para abrir uma nova janela
botao = tk.Button(janela_principal, text="Abrir Nova Janela", command=abrir_nova_janela)
botao.pack(pady=50)

# Inicia o loop principal
janela_principal.mainloop()