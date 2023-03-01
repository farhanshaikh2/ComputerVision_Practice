import argparse
import cv2

parser = argparse.ArgumentParser()

parser.add_argument("output_video_path", help="path to the video file")

args = parser.parse_args()

capture = cv2.VideoCapture(0)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_fps = capture.get(cv2.CAP_PROP_FPS)

# print these values
print(f"width of the frame is: {frame_width}")
print(f"height of the frame is: {frame_height}")
print(f"fps  of the frame is: {frame_fps }")

# Now we specify the video codec using FOURCC, afour byte code.
# Remember, it is platform-dependent. In this case, we define the codec as XVID

fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object. We use the same properties as the input camera.
out_gray = cv2.VideoWriter(args.output_video_path, fourcc, int(
    frame_fps), (int(frame_width), int(frame_height)), False)


if capture.isOpened() is False:
    print("Error opening the video file")


while capture.isOpened():
    ret, frame = capture.read()

    if ret is True:

        # Convert the frame to gray_scale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write the grayscale to windows
        out_gray.write(gray_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break


capture.release()
out_gray.release()
cv2.destroyAllWindows()
