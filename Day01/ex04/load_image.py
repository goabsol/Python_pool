from PIL import Image
import os


def ft_load(path: str) -> Image.Image:
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("File format is not JPG or JPEG.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        return img
    except AssertionError as error:
        print("AssertionError:", error)
        return []
