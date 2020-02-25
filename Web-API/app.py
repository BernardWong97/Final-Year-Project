import sys
import threading

sys.path.append(r'D:\Final-Year-Project\Object-tracking')
print(sys.path)
from frame_detector import LiveDetector
from flask import Flask, render_template, Response
import cv2

# Initialize flask
app = Flask("__main__")

# Initialize camera
video_capture = cv2.VideoCapture(0)
video_capture.set(3, 960)
video_capture.set(4, 540)
video_capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)


def generate():
    global video_capture

    while True:
        ret, frame = video_capture.read()

        outputImg = LiveDetector().track_objects(frame)

        (ret, encodedImg) = cv2.imencode(".jpg", outputImg)

        yield (b'--frame\r\n' 
               b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImg) + b'\r\n')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == '__main__':
    thread = threading.Thread(target=generate)
    thread.daemon = True
    thread.start()
    app.run(debug=True, threaded=True)

video_capture.release()
