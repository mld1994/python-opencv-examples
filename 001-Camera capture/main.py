import os
try:
    import cv2
    print("OpenCV is installed and available!")
except ImportError:
    print("OpenCV is not installed. Please install it using 'pip install opencv-python'")
    os.exit()
    
def get_connected_cameras():
    connected_cameras = []
    index = 0
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if not cap.isOpened():
            break
        connected_cameras.append(index)
        cap.release()
        index += 1
    return connected_cameras

def capture_from_camera(camera_index=0):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_index}.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Camera', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()
    
def main_loop():
    connected_cameras = get_connected_cameras()
    camera_index = 0
    if len(connected_cameras) == 0:
        print("No cameras are connected.")
        return
    elif len(connected_cameras) == 1:
        print("Only one camera is connected.")
        camera_index = connected_cameras[0]
    else:
        print(f"Connected cameras: {connected_cameras}")
        camera_index = int(input("Enter the camera index: "))
        
    capture_from_camera(camera_index)
    
if __name__ == "__main__":
    main_loop()