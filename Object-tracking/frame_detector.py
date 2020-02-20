import cv2
from PIL import Image
from imageai.Detection import ObjectDetection
from centroid_tracker import CentroidTracker

# Instantiate detector and activate webcam
detector = ObjectDetection()
video_capture = cv2.VideoCapture(0)
video_capture.set(3, 960)
video_capture.set(4, 540)
video_capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)

# Set and load model
model_path = "models/yolo.h5"
# input_path = "./input/test4.png"
# output_path = "./output/results4.png"
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

# Set custom objects
custom_objects = detector.CustomObjects(car=True, motorcycle=True, person=True, bicycle=True, dog=True)

# Image object detection
# detections = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

tracker = CentroidTracker()

# Webcam live object detection
# While loop webcam each frame
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # If capture returns true
    if ret:
        rects = []
        text = ""
        x, y = 0, 0
        img = Image.fromarray(frame)
        returned_image, detection = detector.detectCustomObjectsFromImage(custom_objects=custom_objects,
                                                                          input_image=img,
                                                                          output_type="array",
                                                                          input_type="array")

        for eachObject in detection:
            rects.append(eachObject["box_points"])

            (startX, startY, endX, endY) = eachObject["box_points"]
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            text = eachObject["name"]

        objects = tracker.update(rects)

        if objects is not None:
            for (objectID, centroid) in objects.items():
                # draw both the ID of the object and the centroid of the
                # object on the output frame
                if tracker.disappeared[objectID] < 1:
                    text += " " + str(objectID)
                    cv2.putText(frame, text, (centroid[0] - 30, centroid[1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

        cv2.imshow("Frame", frame)

    # Press q to end feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
