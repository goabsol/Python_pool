from PIL import Image
import os
from numpy import array


def ft_load(path: str) -> list[int | float]:
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("File format is not JPG or JPEG.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        print(
            f"The shape of Image is: ({img.size[1]}, {img.size[0]},"
            + f"{img.layers})"
        )
        img_array = array([[pixel for row in array(img) for pixel in row]])
        print(img_array)
        img.show()
        return array(img)
    except AssertionError as error:
        print("AssertionError:", error)
        return []
