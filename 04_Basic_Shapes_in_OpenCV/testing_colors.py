import cv2
import numpy as np
import matplotlib.pyplot as plt
import constant

print(f"Red: {constant.RED}")


def show_with_matplotlib(image, title):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.title(title)
    plt.show()


colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220),
          'rand': np.random.randint(low=0, high=256, size=(3,)).tolist()}

image = np.zeros((500, 500, 3), dtype=np.uint8)
image[:] = colors['light_gray']
seperation = 40
for key in colors:
    cv2.line(image, (0, seperation), (500, seperation), colors[key], 10)
    seperation += 40

show_with_matplotlib(
    image=image, title="Dictionary with some predifined colors")
