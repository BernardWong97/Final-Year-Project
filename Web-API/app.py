import sys

sys.path.append("../Object-tracking")
from frame_detector import LiveDetector
from flask import Flask, render_template, Response
import cv2

outputFrame = None

# Initialize flask
app = Flask("__main__")

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 960)
video_capture.set(4, 540)
video_capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)


def track():
    global video_capture, outputFrame

    # Webcam live object detection
    # While loop webcam each frame
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # If capture returns true
        if ret:
            outputFrame = frame.copy()


def generate():
    global outputFrame

    while True:
        if outputFrame is None:
            continue

        (ret, encodedImg) = cv2.imencode(".jpg", outputFrame)

        if not ret:
            continue

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImg) + b'\r\n')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    track()
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == '__main__':
    app.run(debug=True)

video_capture.release()
