import cv2


def generate_feed():
    url = "http://192.168.18.3:8080/video"

    capture = cv2.VideoCapture(url)

    while True:
        success, frame = capture.read()

        if not success:
            break

        success, buffer = cv2.imencode('.jpg', frame)
        if not success:
            continue

        yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" +
                buffer.tobytes() +
                b"\r\n"
        )
