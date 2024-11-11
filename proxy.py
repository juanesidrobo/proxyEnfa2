class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        # Simula la carga de una imagen pesada
        print(f"Loading image {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        self._real_image.display()

# Uso del proxy
image = ImageProxy("high_res_photo.png")
image.display()  # Carga y muestra la imagen
