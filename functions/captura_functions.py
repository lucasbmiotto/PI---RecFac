import os
from tkinter import messagebox

def exportar_arquivo():
    # Caminho para o arquivo CSV de origem
    arquivo_origem = os.path.join(os.getcwd(), 'exports', 'dados_rosto.csv')

    if not os.path.exists(arquivo_origem):
        messagebox.showerror("Erro", "Arquivo 'dados_rosto.csv' não encontrado!")
        return

    # Caminho para a pasta Downloads do usuário
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    caminho_destino = os.path.join(pasta_downloads, "dados_rosto.csv")

    try:
        with open(arquivo_origem, 'rb') as origem, open(caminho_destino, 'wb') as destino:
            destino.write(origem.read())
        messagebox.showinfo("Sucesso", f"Arquivo exportado para: {caminho_destino}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar o arquivo: {e}")
