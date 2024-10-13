import sqlite3
from tkinter import messagebox

def check_login(username, password):
    conn = sqlite3.connect('database/login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def on_login(entry_1, entry_2, window, abrir_tela_captura):
    username = entry_2.get()
    password = entry_1.get()
    if check_login(username, password):
        messagebox.showinfo("Login Successful", "Welcome!")
        window.destroy()
        abrir_tela_captura()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
