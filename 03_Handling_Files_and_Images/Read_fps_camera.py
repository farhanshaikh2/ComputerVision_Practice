import cv2
import argparse
import time

# We first create the ArgumentParser object
# The created object 'parser' will have the necessary information
# to parse the command-line arguments into data types.
parser = argparse.ArgumentParser()


# We add 'index_camera' argument using add_argument() including a help.
parser.add_argument(
    "index_camera", help="Index of the camera to read from", type=int)
args = parser.parse_args()

# We create a VideoCapture object to read from the camera (pass 0):
capture = cv2.VideoCapture(args.index_camera)

# Get some properties of VideoCapture (frame width, frame height and frames per second (fps)):
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_fps = capture.get(cv2.CAP_PROP_FPS)

# Print these values:
print(f"width of the frame is: {frame_width}")
print(f"height of the frame is: {frame_height}")
print(f"fps of the frame is: {frame_fps}")

# Check if camera opened successfully
if capture.isOpened is False:
    print("Camera is not opened")

while capture.isOpened:
    ret, frame = capture.read()
    if ret:
        # Note the time before processing the frame:
        processing_start = time.time()

        # Convert the frame captured from the camera to grayscale:
        cv2.imshow("Display the capture frame",frame)

        # Display the grayscale frame:
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow("Display the gray image",gray_image)

        # Press q on keyboard to exit the program:
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        # Note the time after processing the frame:
        processing_end = time.time()

        # Calculate the time after processing the frame
        processing_time_frame = processing_end-processing_start

        # FPS = 1 / time per frame
        print(f"FPS is : {1.0 / processing_time_frame}")

    else:
        break

# Release everything:
capture.release()
cv2.destroyAllWindows()
