import cv2

def main():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: no se pudo abrir la cámara")
        return

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: no se pudo leer el frame")
            break

        cv2.imshow("Cam Test", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()