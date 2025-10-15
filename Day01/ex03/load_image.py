from PIL import Image
import os


def ft_load(path: str) -> Image.Image:
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("File format is not JPG or JPEG.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        print(
            f"The shape of Image is: ({img.size[1]}, {img.size[0]}, {img.layers})"
            )
        return img
    except AssertionError as error:
        print("AssertionError:", error)
        return []
