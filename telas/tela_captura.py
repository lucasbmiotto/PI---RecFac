from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog
from telas.tela_camera import abrir_tela_camera
# from functions.camera_functions import NOME_DA_FUNCTIONS_FUTURA --> ATUALIZAR AQUI QUANDO CRIAR A FUNÇÃO DE EXPORT
from functions.captura_functions import exportar_arquivo

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vicre\Documents\GitHub\PI-RecFac-certo\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Função para exportar o arquivo
def exportar_arquivo():
    # Usar filedialog para escolher onde salvar o CSV
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv", 
        filetypes=[("CSV Files", "*.csv")],
        title="Escolha o local para salvar o arquivo",
        initialfile="Dados REC-FAC.csv"  # Nome padrão para o arquivo
    )

    if file_path:
        # Aqui você pode adicionar o código para exportar os dados para o CSV
        # Exemplo de como exportar os dados, ajustando conforme a lógica de captura dos dados
        # Exemplo de exportação:
        # df.to_csv(file_path, index=False)
        print(f"Arquivo exportado para: {file_path}")  # Apenas para exibir onde o arquivo foi salvo

        # Após exportar o arquivo, abre a tela de gráficos
        abrir_tela_graficos()  # Abre a tela de gráficos

# IMPORTANTE! TUDO ESTÁ NESSA FUNÇÃO, PARA QUE A TELA LOGIN POSSA CHAMAR ESSA TELA
def abrir_tela_captura():
    window = Tk()
    window.geometry("1195x797")
    window.configure(bg="#FFFFFF")
    window.title("SAD-RF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=797,
        width=1195,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1195.0,
        129.0,
        fill="#272727",
        outline=""
    )

    # Imagem da logo na parte de cima da tela
    image_logo_captura = PhotoImage(file=relative_to_assets("logo_captura.png"))
    canvas.create_image(
        86.0,
        72.0,
        image=image_logo_captura
    )

    # Quadrado preto da parte de baixo
    canvas.create_rectangle(
        0.0,
        743.0,
        1195.0,
        797.0,
        fill="#272727",
        outline=""
    )

    canvas.create_text(
        432.0,
        761.0,
        anchor="nw",
        text="© 2024 - Todos os direitos reservados a SAD-RF",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    # Botão para exportar para CSV
    button_botao_csv = PhotoImage(file=relative_to_assets("botao_csv.png"))
    button_1 = Button(
        image=button_botao_csv,
        borderwidth=0,
        highlightthickness=0,
        command=exportar_arquivo,  # Chama a função para exportar os dados e abrir a tela de gráficos
        relief="flat"
    )
    button_1.place(
        x=448.0,
        y=271.0,
        width=298.0,
        height=49.0
    )

    # Botão de Captura de dados
    button_botao_captura = PhotoImage(file=relative_to_assets("botao_captura.png"))
    button_3 = Button(
        window,
        image=button_botao_captura,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [window.destroy()],
        relief="flat"
    )
    button_3.place(
        x=450.0,
        y=461.0,
        width=296.0,
        height=85.0
    )

    window.resizable(False, False)
    window.mainloop()
