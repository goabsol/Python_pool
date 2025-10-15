from load_image import ft_load
from numpy import array
import matplotlib.pyplot as plt

img = ft_load("animal.jpeg")
if img:
    img_array = array([[pixel for row in array(img) for pixel in row]])
    print(img_array)
    cropped_img = img.crop((450, 100, 850, 500)).convert("L")
    print(f"New shape after slicing: {cropped_img.size}")
    img_array = array([[[pixel] for row in array(cropped_img) for pixel in row]])
    print(img_array)
    plt.imshow(cropped_img, cmap='gray')
    plt.title("Zoomed Image")
    plt.show()

else:
    print("Failed to load image.")
