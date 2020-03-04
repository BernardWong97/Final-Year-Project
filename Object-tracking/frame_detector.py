import cv2
from PIL import Image
from imageai.Detection import ObjectDetection
from centroid_tracker import CentroidTracker


class LiveDetector:
    def __init__(self):
        # Instantiate detector
        self.detector = ObjectDetection()

        # Set and load model
        self.model_path = "D:/Final-Year-Project/Object-tracking/models/yolo.h5"
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
        names = []
        data = {}
        returned_image, detection = self.detector.detectCustomObjectsFromImage(custom_objects=self.custom_objects,
                                                                               input_image=frame,
                                                                               output_type="array",
                                                                               input_type="array")

        for eachObject in detection:
            rects.append(eachObject["box_points"])
            names.append(eachObject["name"])

            (startX, startY, endX, endY) = eachObject["box_points"]
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            w, h = endX - startX, endY - startY

            ROI = frame[startY:startY + h, startX:startX + w]
            blur = cv2.GaussianBlur(ROI, (11, 11), 0)

            frame[startY:startY + h, startX:startX + w] = blur

        objects = self.tracker.update(rects, names)

        if objects is not None:
            for objectID, objectDetails in objects.items():
                # draw both the ID of the object and the centroid of the
                # object on the output frame
                centroid = objectDetails[0]
                name = objectDetails[1]
                if self.tracker.disappeared[objectID] < 1:
                    text = name + " " + str(objectID)
                    cv2.putText(frame, text, (centroid[0] - 30, centroid[1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

                    data[name] = objectID

        return frame, data
