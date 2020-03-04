import cv2
from frame_detector import LiveDetector


class Test:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.video_capture.set(3, 960)
        self.video_capture.set(4, 540)
        self.video_capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        self.detector = LiveDetector()
        self.frame = None

    def run(self):
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.draw_circle)

        while True:
            ret, frame = self.video_capture.read()

            outputImg, data = self.detector.track_objects(frame)
            self.frame = outputImg
            cv2.circle(self.frame, (0, 2), 4, (0, 255, 0), -1)
            cv2.imshow("image", self.frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def draw_circle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(self.frame, (x, y), 100, (255, 0, 0), 2)
            print(x, y)


test = Test()
test.run()
test.video_capture.release()
cv2.destroyAllWindows()
