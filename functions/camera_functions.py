import cv2
from PIL import Image, ImageTk

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
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.itemconfig(self.image_id, image=img)
            self.canvas.image = img

        self.canvas.after(50, self.update_frame)

    def release(self):
        self.cap.release()