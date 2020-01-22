from imageai.Detection import VideoObjectDetection
from matplotlib import pyplot as plt
import cv2

# Instantiate detector and activate webcam
detector = VideoObjectDetection()
video_capture = cv2.VideoCapture(0)

model_path = "./models/yolo.h5"
# input_path = "./input/test4.png"
# output_path = "./output/results4.png"

detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

custom_objects = detector.CustomObjects(car=True, motorcycle=True, person=True, bicycle=True, truck=True, dog=True)
color_index = {'car': 'red', 'motorcycle': 'orange', 'truck': 'yellow', 'bicycle': 'beige', 'person': 'blue', 'dog': 'green'}


def forFrame(frame_number, output_array, output_count, returned_frame):
    plt.clf()

    this_colors = []
    labels = []
    sizes = []

    counter = 0

    for eachItem in output_count:
        counter += 1
        labels.append(eachItem + " = " + str(output_count[eachItem]))
        sizes.append(output_count[eachItem])
        this_colors.append(color_index[eachItem])

    plt.subplot(1, 2, 1)
    plt.title("Frame : " + str(frame_number))
    plt.axis("off")
    plt.imshow(returned_frame, interpolation="none")

    plt.subplot(1, 2, 2)
    plt.title("Analysis: " + str(frame_number))
    plt.pie(sizes, labels=labels, colors=this_colors, shadow=True, startangle=140, autopct="%1.1f%%")

    plt.pause(0.01)


plt.show()

video_path = detector.detectCustomObjectsFromVideo(camera_input=video_capture,
                                                   save_detected_video=False,
                                                   frames_per_second=60,
                                                   log_progress=False,
                                                   per_frame_function=forFrame,
                                                   return_detected_frame=True,
                                                   minimum_percentage_probability=70)

# Image object detection
# detections = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
#
# for eachObject in detections:
#     print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
#     print("--------------------------------")
