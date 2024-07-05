import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    global face_cascade    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))    
    return faces

def main_loop():
    global detected_faces

    cap = cv2.VideoCapture(0)
    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        faces = detect_faces(frame)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Camera', frame)
        
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_loop()