import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from telas.tela_captura import abrir_tela_captura
from functions.login_functions import on_login, check_login

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vicre\Documents\GitHub\PI-RecFac-certo\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_enter(event):
    on_login(entry_1, entry_2, window, abrir_tela_captura)
    mostrar_animacao_sucesso()  # Mostrar animação de sucesso após login

def mostrar_animacao_sucesso():
    # Criando animação de sucesso (um texto que aparece e desaparece)
    texto_sucesso = canvas.create_text(
        375, 400,  # Posição do texto
        text="Login bem-sucedido!",
        fill="#28a745",  # Cor verde
        font=("Arial", 24, "bold")
    )

    # Animação de transição (desaparece após 2 segundos)
    canvas.after(2000, canvas.delete, texto_sucesso)  # Apagar o texto após 2 segundos

def abrir_tela_login():
    global entry_1, entry_2, window, canvas

    window = Tk()
    window.geometry("750x700")
    window.configure(bg="#FFFFFF")
    window.title("SAD-RF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=630,
        width=750,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    logo_login = PhotoImage(file=relative_to_assets("logo_login.png"))
    canvas.create_image(375.0, 186.0, image=logo_login)

    campo_login = PhotoImage(file=relative_to_assets("campo_login2.png"))
    canvas.create_image(375.0, 395.0, image=campo_login)
    entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=259.0, y=376.0, width=232.0, height=39.0)

    campo_senha = PhotoImage(file=relative_to_assets("campo_login1.png"))
    canvas.create_image(375.0, 450.0, image=campo_senha)
    entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show="*")
    entry_1.place(x=259.0, y=430.0, width=232.0, height=39.0)

    botao_entrar_login = PhotoImage(file=relative_to_assets("botao_entrar_login.png"))
    button_1 = Button(
        image=botao_entrar_login,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_login(entry_1, entry_2, window, abrir_tela_captura),
        relief="flat"
    )
    button_1.place(x=250.0, y=530.0, width=241.0, height=50.0)

    window.bind('<Return>', on_enter)

    window.resizable(False, False)
    window.mainloop()
