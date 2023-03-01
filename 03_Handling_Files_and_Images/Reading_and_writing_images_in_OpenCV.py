import cv2
import argparse

# Create an object for argparse
parser = argparse.ArgumentParser()

# Add an image_input_path and image_output_path to add_argument()
parser.add_argument("image_input_path",
                    help="path to input image to be displayed")
parser.add_argument("image_output_path",
                    help="path to output(processed) image to be displayed")

# Parse the argument and store it in a dictionary:
args = vars(parser.parse_args())

# we can load the input image from disk:
image_input = cv2.imread(args["image_input_path"])

# Show the loaded image
cv2.imshow("loaded_image", image_input)

# Process the input image (In this example we are just converting it into grayscale):
gray_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)

# Show the processed image:
cv2.imshow("Gray image", gray_image)

# save the processed image to disk:
cv2.imwrite(args["image_output_path"], gray_image)

# Wait until the key is pressed:
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
