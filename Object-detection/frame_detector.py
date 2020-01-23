from imageai.Detection import ObjectDetection
from PIL import Image
import cv2

# Instantiate detector and activate webcam
detector = ObjectDetection()
video_capture = cv2.VideoCapture(0)

# Set and load model
model_path = "./models/yolo.h5"
# input_path = "./input/test4.png"
# output_path = "./output/results4.png"
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

# Set custom objects
custom_objects = detector.CustomObjects(car=True, motorcycle=True, person=True, bicycle=True, truck=True, dog=True)

# Image object detection
# detections = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

# Webcam live object detection
# While loop webcam each frame
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # If capture returns true
    if ret:
        img = Image.fromarray(frame)
        returned_image, detection = detector.detectCustomObjectsFromImage(custom_objects=custom_objects,
                                                                          input_image=img,
                                                                          output_type="array",
                                                                          input_type="array")
        cv2.imshow("webcam", returned_image)

        for eachObject in detection:
            print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
            print("--------------------------------")

    # Press q to end feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
