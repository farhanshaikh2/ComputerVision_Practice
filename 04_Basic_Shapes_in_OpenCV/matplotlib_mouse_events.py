import cv2
import numpy as np
import matplotlib.pyplot as plt

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}


image = np.zeros((400, 400, 3), dtype=np.uint8)

image[:] = colors['light_gray']


def upload_image_with_matplotlib():
    image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_RGB)
    figure.canvas.draw()


def click_mouse_event(event):
    cv2.circle(image,
               (int(round(event.xdata)), int(round(event.ydata))),
               30, colors['red'], -1)
    upload_image_with_matplotlib()


figure = plt.figure()
figure.add_subplot(111)

upload_image_with_matplotlib()

figure.canvas.mpl_connect('button_press_event', click_mouse_event)


plt.show()
