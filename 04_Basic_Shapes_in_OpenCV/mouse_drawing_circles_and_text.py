import cv2
import numpy as np

# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# Create a mouse callback function


def draw_text():
    # Set the position to be used for drawing text:
    menu_position = (10, 500)
    menu_position1 = (10, 525)
    menu_position2 = (10, 550)
    menu_position3 = (10, 575)

    # write the menu
    cv2.putText(image, 'Double left click: add a circle',
                menu_position, cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors['white'])
    cv2.putText(image, 'Simple right click:delete lat circle',
                menu_position1, cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors['white'])
    cv2.putText(image, 'Double right click: delete all circle',
                menu_position2, cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors['white'])
    cv2.putText(image, 'Press \'q\' to exit',
                menu_position3, cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors['white'])

# mouse callback function:


def draw_circle(event, x, y, flags, param):
    global circles

    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Add the circle with coordinates x,y
        print("event: EVENT_LBUTTONDBLCLK")
        circles.append((x, y))

    if event == cv2.EVENT_RBUTTONDBLCLK:
        # Delete all circles (clean the screen)
        print("event: EVENT_RBUTTONDBLCLK")
        circles[:] = []
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Delete last added circle
        print("event: RBUTTONDOWN")
        try:
            circles.pop()
        except (IndexError):
            print("No circle to delete")
    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")


# Structure to hold the created circles:
circles = []

# Create a canvas of 600 x 600, 3 channels
image = np.zeros((600, 600, 3), dtype=np.uint8)

# We create a named window where the mouse callback will be established
cv2.namedWindow("Image Mouse")

# Set a mouse callback function
cv2.setMouseCallback("Image Mouse", draw_circle)

# We draw the menu
draw_text()

# we get a copy with only the text printed on it.
clone = image.copy()

while True:
    image = clone.copy()

    # we draw now only the current circle:
    for pos in circles:
        cv2.circle(image, pos, 30, colors['blue'], -1)

    # Show image 'Image mouse':
    cv2.imshow('Image mouse', image)

    # Continue until 'q' is pressed:
    if cv2.waitKey(400) & 0xFF == ord('q'):
        break

# Destroy all generated windows:
cv2.destroyAllWindows()
