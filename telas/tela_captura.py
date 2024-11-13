from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from telas.tela_camera import abrir_tela_camera
# from functions.camera_functions import NOME_DA_FUNCTIONS_FUTURA --> ATUALIZAR AQUI QUANDO CRIAR A FUNÇÃO DE EXPORT
from functions.captura_functions import exportar_arquivo

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Docs\PI-RecFac\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
        command=exportar_arquivo,
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
        command=lambda: [window.destroy(), abrir_tela_camera()],
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