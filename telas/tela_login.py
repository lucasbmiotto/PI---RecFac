import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from tela_captura import abrir_tela_captura 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vicre\Documents\GitHub\PI-RecFac\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_login(username, password):
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def on_login():
    username = entry_1.get()
    password = entry_2.get()
    if check_login(username, password):
        messagebox.showinfo("Login Successful", "Welcome!")
        window.destroy()  
        abrir_tela_captura()  
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

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

# Logo
canvas.place(x=0, y=0)
logo_login = PhotoImage(file=relative_to_assets("logo_login.png"))
canvas.create_image(375.0, 186.0, image=logo_login)

# Campo Login
campo_login = PhotoImage(file=relative_to_assets("campo_login.png"))
canvas.create_image(375.0, 450.0, image=campo_login)
entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=259.0, y=430.0, width=232.0, height=39.0)

# Campo Senha
campo_senha = PhotoImage(file=relative_to_assets("campo_senha.png"))
canvas.create_image(375.0, 395.0, image=campo_senha)
entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show="*")
entry_2.place(x=259.0, y=376.0, width=232.0, height=39.0)

# Botão Entrar
botao_entrar_login = PhotoImage(file=relative_to_assets("botao_entrar_login.png"))
button_1 = Button(
    image=botao_entrar_login,
    borderwidth=0,
    highlightthickness=0,
    command=on_login,
    relief="flat"
)
button_1.place(x=250.0, y=530.0, width=241.0, height=50.0)

window.resizable(False, False)
window.mainloop()
