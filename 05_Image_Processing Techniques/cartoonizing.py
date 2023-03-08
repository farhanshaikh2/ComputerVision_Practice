"""
Cartoonizing images using both custom and OpenCV functions
"""

# Import required packages:
import cv2
import matplotlib.pyplot as plt


def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(2, 4, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


plt.figure(figsize=(14, 6))
plt.suptitle("Cartoonizing images", fontsize=14, fontweight='bold')

image = cv2.imread('05_Image_Processing Techniques\Faiz logo photo.jpg')


sketch_gray, sketch_color = cv2.pencilSketch(
    image, sigma_s=30, sigma_r=0.1, shade_factor=0.1)
stylizated_image = cv2.stylization(image, sigma_s=90, sigma_r=0.09)


show_with_matplotlib(image, "Original", 1)
show_with_matplotlib(cv2.cvtColor(
    sketch_gray, cv2.COLOR_GRAY2BGR), "sketch_gray", 2)
show_with_matplotlib(sketch_color, "sketch_color", 3)
show_with_matplotlib(stylizated_image, "stylizated_image", 4)


plt.show()
