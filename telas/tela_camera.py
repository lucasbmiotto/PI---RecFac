from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\dudug\Desktop\REC-FAC\PI-RecFac\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# ------------------------------ FUNÇÕES DE CAMERA ------------------------------

class CameraApp:
    def __init__(self, canvas, image_id):
        self.canvas = canvas
        self.image_id = image_id
        self.cap = cv2.VideoCapture(0)
        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Processa o frame, se necessário
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))

            # Atualiza a imagem no canvas
            self.canvas.itemconfig(self.image_id, image=img)
            self.canvas.image = img

        # Chama a função novamente após 50 ms
        self.canvas.after(50, self.update_frame)

    def release(self):
        self.cap.release()

# ------------------------- FIM DAS FUNÇÕES DE CAMERA -------------------------

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

    # Botão parar Captura de dados
    button_botao_captura = PhotoImage(file=relative_to_assets("botao_captura.png"))
    button_2 = Button(
        image=button_botao_captura,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [camera_app.release(), window.destroy(), abrir_tela_captura()],
        relief="flat"
    )
    button_2.place(
        x=450.0,
        y=580.0,
        width=296.0,
        height=85.0
    )

    # Cria a imagem onde a câmera será exibida
    image_image_2 = PhotoImage(file=relative_to_assets("quadrado_camera.png"))
    image_id = canvas.create_image(597.0, 340.0, image=image_image_2)

    camera_app = CameraApp(canvas, image_id)

    def on_closing():
        camera_app.release()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Essa importação fica dentro da função, para evitar "Importação circular"
    from telas.tela_captura import abrir_tela_captura

    window.resizable(False, False)
    window.mainloop()