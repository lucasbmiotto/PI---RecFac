# tela_login.py
import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from telas.tela_captura import abrir_tela_captura  # Ajuste a importação aqui

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\22.01388-0\Documents\PI-RecFac\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_login(username, password):
    conn = sqlite3.connect('database/login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def on_login():
    username = entry_2.get()
    password = entry_1.get()
    if check_login(username, password):
        messagebox.showinfo("Login Successful", "Welcome!")
        window.destroy()
        abrir_tela_captura()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def on_enter(event):
    on_login()

def abrir_tela_login():
    global entry_1, entry_2, window  # Tornando as entradas e a janela globais

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
        command=on_login,
        relief="flat"
    )
    button_1.place(x=250.0, y=530.0, width=241.0, height=50.0)

    window.bind('<Return>', on_enter)

    window.resizable(False, False)
    window.mainloop()
