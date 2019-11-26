from imageai.Detection import ObjectDetection
from PIL import Image

detector = ObjectDetection()

model_path = "./models/yolo.h5"
input_path = "./input/test3.png"
output_path = "./output/result3.png"

detector.setModelTypeAsYOLOv3()

detector.setModelPath(model_path)

detector.loadModel()

detections = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")
