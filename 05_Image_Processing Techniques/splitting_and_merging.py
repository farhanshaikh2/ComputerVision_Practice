import cv2
import matplotlib.pyplot as plt


def show_with_matplotlib(image, title, position):
    # Convert the image from BGR to RGB
    image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    ax = plt.subplot(3, 6, position)
    plt.imshow(image_RGB)
    plt.title(title)
    plt.axis('off')


image = cv2.imread('color_spaces.png')
