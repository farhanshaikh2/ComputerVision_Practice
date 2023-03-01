import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "index_camera", help="index of the camera to read from", type=int)

args = parser.parse_args()

capture = cv2.VideoCapture(args.index_camera)

height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = capture.get(cv2.CAP_PROP_FPS)

print(f"Height of the frame is :{height}")
print(f"width of the frame is :{width}")
print(f"fps of the frame is :{fps}")

# Check whether the camera is opened
if capture.isOpened() is False:
    print("Error opening camera")

# Index to save frame
frame_index = 0

while capture.isOpened():
    ret, frame = capture.read()

    if ret:
        # Display the capture image
        cv2.imshow("Input frame from the camera", frame)

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale frame:
        cv2.imshow("Gray frame image", gray_frame)

        # Press 'c' on the keyboard to exit the program
        if cv2.waitKey(20) & 0xFF == ord('c'):
            frame_name = f"camera_frame_{frame_index}.png"
            gray_frame_index = f"grayscale_camera_frame_{frame_index}.png"
            cv2.imwrite(frame_name, frame)
            cv2.imwrite(gray_frame_index, gray_frame)
            frame_index += 1

    else:
        break

capture.release()
cv2.destroyAllWindows()
