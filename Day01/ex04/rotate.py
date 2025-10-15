from load_image import ft_load
from numpy import array
import matplotlib.pyplot as plt
from PIL import Image


def transpose_image(img):
    w, h = img.size
    transposed_img = Image.new("RGB", (h, w))

    for y in range(h):
        for x in range(w):
            pixel = img.getpixel((x, y))
            transposed_img.putpixel((y, x), pixel)

    return transposed_img


img = ft_load("animal.jpeg")
if img:
    cropped_img = img.crop((450, 100, 850, 500))
    print(f"New shape after slicing: {cropped_img.size}")
    img_array = array(
        [[[pixel] for row in array(cropped_img.convert("L"))
          for pixel in row]]
    )
    print(img_array)
    transposed_img = transpose_image(cropped_img).convert("L")
    print(f"New shape after Transpose: {transposed_img.size}")
    print(array(transposed_img))
    img_array = array([[[pixel] for row in array(transposed_img)
                        for pixel in row]])
    plt.imshow(transposed_img, cmap="gray")
    plt.title("Zoomed Image")
    plt.show()

else:
    print("Failed to load image.")
