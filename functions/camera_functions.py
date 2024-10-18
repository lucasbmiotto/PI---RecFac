import cv2
import os
from PIL import Image, ImageTk
import datetime
from deepface import DeepFace

class CameraApp:
    def __init__(self, canvas, image_id):
        self.canvas = canvas
        self.image_id = image_id
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        if not os.path.exists("rostos"):
            os.makedirs("rostos")

        self.face_detected = False
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(rgb_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    # Se não houver foto tirada, tirar uma foto
                    if not self.face_detected:
                        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                        photo_path = os.path.join("rostos", f"rosto_{timestamp}.jpg")
                        cv2.imwrite(photo_path, frame)
                        self.face_detected = True

                        # Analisar a imagem e coletar dados
                        self.analise_face(photo_path)

                        # Mudar o retângulo para vermelho
                        cv2.rectangle(rgb_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            else:
                # Se nenhum rosto for detectado, resetar a variável de controle
                self.face_detected = False

            # Converter a imagem para o formato Tkinter
            img = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
            self.canvas.itemconfig(self.image_id, image=img)
            self.canvas.image = img

        self.canvas.after(50, self.update_frame)

    def analise_face(self, photo_path):
        # Analisar a imagem usando o DeepFace
        try:
            analysis = DeepFace.analyze(photo_path, actions=['age', 'gender', 'race', 'emotion'])
            data = analysis[0]  # Pegando os dados do primeiro rosto detectado

            # Coletar os dados
            age = data['age']
            gender = data['gender']
            race = data['dominant_race']
            emotion = data['dominant_emotion']

            # Criar e salvar os dados em um arquivo .txt
            with open('dados_rosto.txt', 'a') as f:
                f.write(f"Foto: {photo_path}\n")
                f.write(f"Idade: {age}\n")
                f.write(f"Gênero: {gender}\n")
                f.write(f"Raça: {race}\n")
                f.write(f"Emoção: {emotion}\n\n")

            # Deletar a imagem após a análise
            os.remove(photo_path)

        except Exception as e:
            print(f"Erro na análise do rosto: {e}")

    def release(self):
        self.cap.release()
