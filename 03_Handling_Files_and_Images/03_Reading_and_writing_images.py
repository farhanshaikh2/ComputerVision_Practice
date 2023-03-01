import argparse
import cv2

parser = argparse.ArgumentParser()

# Default type of add_argument is string.
parser.add_argument("path_image", help="path to input image to be displayed")

# The information about arguments is stored in 'parser'
# Then it is used when the parser calls 'parse_args()'
args = parser.parse_args()

# We can load the input image from disk:
image = cv2.imread(args.path_image)

# Parse the argument and store it in a dictionary:
args = vars(parser.parse_args())

# Now, we can also load the image from disk using args:
image2 = cv2.imread(args["path_name"])

# Show the loaded image
cv2.imshow("loaded_image", image)
cv2.imshow("loaded_image2", image2)

# Wait until key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
