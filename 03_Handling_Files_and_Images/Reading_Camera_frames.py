import cv2
import argparse

# Create an object for argparse
parser = argparse.ArgumentParser()

# Add an image_input_path and image_output_path to add_argument()
parser.add_argument("index_camera",
                    help="index of the camera to read from", type=int)

# Parse the argument and store it in a dictionary:
args = parser.parse_args()

# We create a VideoCapture object to read from the camera (pass 0)
capture = cv2.VideoCapture(args.index_camera)

# Get some properties of VideoCapture (frame width,frame height and frames per second (fps))
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# Print these values:
print(f"Frame Width: {frame_width}")
print(f"Frame Height: {frame_height}")
print(f"Frames per second: {fps}")

# Check if camera is opened succesfully.
if capture.isOpened() is False:
    print("Error opening the camera")

# Read until video is completed
while capture.isOpened():
    # Capture frame by frame from the camera
    ret, frame = capture.read()

    if ret is True:
        # Display the capture frame:
        cv2.imshow("Input frame from the camera", frame)

        # Convert the frame captured from camera to grayscale:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the gray_scale image
        cv2.imshow("Grayscale input camera", gray_frame)

        # Press q on keyboard to exit the program
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything
capture.release()
cv2.destroyAllWindows()
