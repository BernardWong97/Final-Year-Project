import cv2
import numpy as np
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
        frame = self.pixelate_frontyard((100, 100), frame)

        returned_image, detection = self.detector.detectCustomObjectsFromImage(custom_objects=self.custom_objects,
                                                                               input_image=frame,
                                                                               output_type="array",
                                                                               input_type="array")
        for eachObject in detection:
            rects.append(eachObject["box_points"])
            names.append(eachObject["name"])

            (startX, startY, endX, endY) = eachObject["box_points"]
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            self.blur_object((startX, startY), (endX, endY), (11, 11), frame)

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

    def blur_object(self, topLeft, bottomRight, kSize, frame):
        x, y = topLeft[0], topLeft[1]
        w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

        ROI = frame[y:y + h, x:x + w]
        blur = cv2.GaussianBlur(ROI, kSize, 0)

        frame[y:y + h, x:x + w] = blur

    def blur_frontyard(self, kSize, frame):
        height, width, channel = frame.shape
        ROI_corners = np.array([[(320, 490), (895, 320), (895, height), (320, height)]], dtype=np.int32)
        blurred_frame = cv2.GaussianBlur(frame, kSize, 0)
        mask = np.zeros(frame.shape, dtype=np.uint8)
        ignore_mask_color = (255,) * channel
        cv2.fillPoly(mask, ROI_corners, ignore_mask_color)
        mask_inverse = np.ones(mask.shape).astype(np.uint8) * 255 - mask
        frame = cv2.bitwise_and(blurred_frame, mask) + cv2.bitwise_and(frame, mask_inverse)

        return frame

    def pixelate_frontyard(self, kSize, frame):
        height, width, channel = frame.shape
        w, h = kSize
        ROI_corners = np.array([[(320, 490), (895, 320), (895, height), (320, height)]], dtype=np.int32)
        temp = cv2.resize(frame, (w, h), interpolation=cv2.INTER_LINEAR)
        pixelated_frame = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
        mask = np.zeros(frame.shape, dtype=np.uint8)
        ignore_mask_color = (255,) * channel
        cv2.fillPoly(mask, ROI_corners, ignore_mask_color)
        mask_inverse = np.ones(mask.shape).astype(np.uint8) * 255 - mask
        frame = cv2.bitwise_and(pixelated_frame, mask) + cv2.bitwise_and(frame, mask_inverse)

        return frame
