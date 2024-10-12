from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Docs\PI-RecFac\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def abrir_tela_camera():
    window = Tk()

    window.geometry("1195x797")
    window.configure(bg="#FFFFFF")

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

    # Botão de Captura de dados
    button_botao_captura = PhotoImage(file=relative_to_assets("botao_captura.png"))
    button_2 = Button(
        image=button_botao_captura,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [window.destroy(), abrir_tela_captura()],  # Vai voltar para a tela_captura
        relief="flat"
    )
    button_2.place(
        x=450.0,
        y=580.0,
        width=296.0,
        height=85.0
    )

    # Imagem onde fica a camera
    image_image_2 = PhotoImage(
        file=relative_to_assets("quadrado_camera.png"))
    image_2 = canvas.create_image(
        597.0,
        340.0,
        image=image_image_2
    )

    # Essa importação fica dentro da função, para evitar "Importação circular", dps eu explico isso
    from telas.tela_captura import abrir_tela_captura

    window.resizable(False, False)
    window.mainloop()
