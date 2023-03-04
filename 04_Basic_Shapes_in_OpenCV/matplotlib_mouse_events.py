import cv2
import numpy as np
import matplotlib.pyplot as plt


colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros((400, 400, 3), dtype=np.uint8)

image[:] = colors['light_gray']


def update_img_with_matplotlib():

    image = image[:, :, ::-1]

    plt.imshow(image)

    figure.canvas.draw()


def click_mouse_event(event):
    cv2.circle(image, (event.xdata, event.ydate), 30, colors['blue'], -1)

    update_img_with_matplotlib()


# we create the figure:
figure = plt.figure()
figure.add_subplot(111)

# To show the image until click is performed:
update_img_with_matplotlib()

figure.canvas.mpl_connect('button_press_event', click_mouse_event)

plt.show()
