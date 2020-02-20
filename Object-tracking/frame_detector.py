import cv2
from PIL import Image
from imageai.Detection import ObjectDetection
from centroid_tracker import CentroidTracker


class LiveDetector:
    def __init__(self):
        # Instantiate detector
        self.detector = ObjectDetection()

        # Set and load model
        self.model_path = "models/yolo.h5"
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(self.model_path)
        self.detector.loadModel()

        # Set custom objects
        self.custom_objects = self.detector.CustomObjects(car=True,
                                                          motorcycle=True,
                                                          person=True,
                                                          bicycle=True,
                                                          dog=True)
        self.tracker = CentroidTracker()

    def track_objects(self, frame):
        rects = []
        text = ""
        x, y = 0, 0
        img = Image.fromarray(frame)
        returned_image, detection = self.detector.detectCustomObjectsFromImage(custom_objects=self.custom_objects,
                                                                               input_image=img,
                                                                               output_type="array",
                                                                               input_type="array")

        for eachObject in detection:
            rects.append(eachObject["box_points"])

            (startX, startY, endX, endY) = eachObject["box_points"]
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            text = eachObject["name"]

        objects = self.tracker.update(rects)

        if objects is not None:
            for (objectID, centroid) in objects.items():
                # draw both the ID of the object and the centroid of the
                # object on the output frame
                if self.tracker.disappeared[objectID] < 1:
                    text += " " + str(objectID)
                    cv2.putText(frame, text, (centroid[0] - 30, centroid[1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

        return frame
