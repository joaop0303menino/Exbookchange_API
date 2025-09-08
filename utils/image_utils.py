from PIL import Image
import io
import os
from pathlib import Path

class ImageUtils:
    def convert_image_to_bytes(self, image: Image.Image, format="PNG"):
        img_byte_arr = io.BytesIO()

        image.save(img_byte_arr, format=format)

        return img_byte_arr.getvalue()

    def convert_bytes_to_image(self, bytes):
        img = Image.open(io.BytesIO(bytes))
        img.load()

        return img

    def save_image_in_server(self, image: Image.Image, file_name: str, format="PNG"):
        path_save = Path("../images_saves") / (Path(file_name).stem + ".png")
        path_save.parent.mkdir(parents=True, exist_ok=True)

        image.save(path_save, format=format)

        return str(path_save)