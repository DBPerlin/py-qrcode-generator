import qrcode
import tkinter as tk
from tkinter import messagebox

def executar_download():
    url = entry_url.get()

    if not url.strip():
        messagebox.showerror("Erro", "Por favor, insira um link válido.")
        return

    try:
        qr = qrcode.make(url)
        qr.save("qrcode.png")

        messagebox.showinfo("Sucesso", "QR Code gerado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar QR Code:\n{e}")


# Criando janela
janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.geometry("400x150")
janela.resizable(False, False)

# Label
label = tk.Label(janela, text="Link do site:")
label.pack(pady=10)

# Input
entry_url = tk.Entry(janela, width=50)
entry_url.pack(pady=5)

# Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=15)

btn_download = tk.Button(frame_botoes, text="Baixar", command=executar_download)
btn_download.grid(row=0, column=0, padx=10)

btn_sair = tk.Button(frame_botoes, text="Sair", command=janela.quit)
btn_sair.grid(row=0, column=1, padx=10)

# Loop da aplicação
janela.mainloop()