import cv2
from PIL import Image, ImageTk
from deepface import DeepFace

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
            # Conversão de BGR para RGB para o DeepFace e Tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Tenta analisar o frame atual usando DeepFace
            try:
                analysis = DeepFace.analyze(frame_rgb, actions=['age', 'gender', 'emotion', 'race'], enforce_detection=False)
                
                # Extrai os resultados da análise
                age = analysis['age']
                gender = analysis['gender']
                dominant_emotion = analysis['dominant_emotion']
                dominant_race = analysis['dominant_race']

                # Escreve os resultados no frame da câmera
                cv2.putText(frame_rgb, f'Age: {int(age)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame_rgb, f'Gender: {gender}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame_rgb, f'Emotion: {dominant_emotion}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame_rgb, f'Race: {dominant_race}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
            except Exception as e:
                print(f"DeepFace analysis failed: {e}")

            # Converte o frame para exibir na interface gráfica (Tkinter)
            img = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
            self.canvas.itemconfig(self.image_id, image=img)
            self.canvas.image = img

        # Atualiza a cada 50ms
        self.canvas.after(50, self.update_frame)

    def release(self):
        self.cap.release()
