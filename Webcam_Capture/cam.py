import cv2

def take_picture():
    # Open the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Read and display frame, then wait for key press
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)

        # Wait for spacebar (ASCII code 32) to be pressed
        if cv2.waitKey(1) & 0xFF == ord(' '):
            # Save the frame as an image file
            cv2.imwrite('captured_image.jpg', frame)
            print("Image captured!")
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    take_picture()
