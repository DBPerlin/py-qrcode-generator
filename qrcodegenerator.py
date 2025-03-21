import qrcode
import PySimpleGUI as sg
import tkinter as tk

def executar_download(url):
    try:
        qr = qrcode.make(url)
        qr.save("qrcode.png")

        print(f"Baixando qrcode")
        print("Download concluido!")
    except Exception as e:
        print(f"Erro ao realizar o download: {e}")


layout = [
    [sg.Text("Link do site: "), sg.InputText(size=(40, 1), key='url')],
    [sg.Button('Baixar'), sg.Button('Sair')],
]

janela = sg.Window('Gerador de QrCode', layout)

while True:
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Baixar':
        url = values['url']
        if url.strip():
            executar_download(url)
            sg.popup_ok("Download realizado com sucesso!")
        else:
            sg.popup_error("Por favor, insira um link valido.")
        
janela.close()