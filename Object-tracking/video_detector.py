from imageai.Detection import VideoObjectDetection
import cv2

# Instantiate detector and activate webcam
detector = VideoObjectDetection()
video_capture = cv2.VideoCapture(0)

# Set and load model
model_path = "models/yolo.h5"
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

# Set custom classes
custom_objects = detector.CustomObjects(car=True, motorcycle=True, person=True, bicycle=True, truck=True, dog=True)


# Functions to parse into the detection for every frame and execute which takes analytical data of the frames.
def forFrame(frame_number, output_array, output_count):
    print("FOR FRAME ", frame_number)
    print("Output for each object : ", output_array)
    print("Output count for unique objects : ", output_count)
    print("------------END OF A FRAME --------------")


def forSeconds(second_number, output_arrays, count_arrays, average_output_count):
    print("SECOND : ", second_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last second: ", average_output_count)
    print("------------END OF A SECOND --------------")


def forMinute(minute_number, output_arrays, count_arrays, average_output_count):
    print("MINUTE : ", minute_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last minute: ", average_output_count)
    print("------------END OF A MINUTE --------------")


def forFull(output_arrays, count_arrays, average_output_count):
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the entire video: ", average_output_count)
    print("------------END OF THE VIDEO --------------")


# Webcam live object detection
video_path = detector.detectCustomObjectsFromVideo(custom_objects=custom_objects,
                                                   camera_input=video_capture,
                                                   output_file_path="output/testvid",
                                                   frames_per_second=20,
                                                   per_second_function=forSeconds,
                                                   minimum_percentage_probability=70,
                                                   detection_timeout=120)
