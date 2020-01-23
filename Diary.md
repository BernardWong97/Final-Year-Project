# Developer's Diary
A diary to record the progress of the project.

## Week 1 (15<sup>th</sup> October 2019 - 21<sup>st</sup> October 2019)
Met supervisor.  
Begin research project idea.  
Interested in:
- React web application framework
- Single-page application
- Machine Learning
- Python
- MVVM/MVC frameworks

Problems encountered:
- Did Angular and Ionic in previous years but limited knowledge
- Only exposed to Machine Learning in this semester
- No real vision on the whole project's structure and functions
- Only encountered TensorFlow Keras in this semester
- Need time to understand Flask framework
- Is the idea enough for final year project credit?

Meeting conclusion:  
Machine Learning Web Application idea is suitable for the project and need to find the context of the project.

## Week 2 (22<sup>nd</sup> October 2019 - 28<sup>th</sup> October 2019)
Decided to create a Machine Learning Web Application:
- Use Python to develop a React web application using Flask framework (Front end)
- Machine Learning (Back end)

Questions:
- What kind of Machine Learning model?
    - Supervised? (Still learning in other modules)
    - Unsupervised (No experience)
    - Train as the project goes go pre-trained model
- What dataset is the application going to deal with?
    - Pre-defined dataset available online (Supervised)
    - Collect data as the project progress (Unsupervised)
    - Heavy time dependent if collecting data from scratch
- Front end User Interface
    - Focus on the model or UI
    - What is the main purpose of the web application
    - User Interaction? or just for display
    - Some kind of form input prediction
    
Ideas on Models:
- Handwriting recognition
- GPS
- ~~Stock~~
- Movies/Music recommender
- Novel

Meeting conclusion:  
If collect data from scratch, need to spend a lot of time to get a decent amount of data. Try to find a pre-defined dataset 
that is available online. Look into TensorFlow or Keras library see if any dataset suitable for the project.

## Week 3 (29<sup>th</sup> October 2019 - 4<sup>th</sup> November 2019)
Unexpected incident occurs, missed the meeting with supervisor.  
Did not have much progress as assignment from other course module are due this week.  

Brainstorming ideas on what functionality should the web application going to have to be useful.
Have a rough idea about the project purpose and structure but need to do more research on it to determine whether it is doable.

## Week 4 (5<sup>th</sup> November 2019 - 11<sup>th</sup> November 2019)
Decided on creating a web application that streams live video feed from a webcam that is located in the room capturing the events 
on the road outside the house. The Machine Learning part is where the application can recognise, track vehicles and collect data from the video feed 
and carry out data analysis. Then display some sort of analysed data as a graph or something on the web page.

Result on research:
- Live streaming video feed and webcam usage
    - Need MongoDB for the stream key to have access to the video feed
    - OBS studio software for streaming
- Object detection
    - Car detection (Not sure do the project need this or let the machine recognise itself as no machine learning is involve)

Meeting conclusion:  
- Try and find a pre-defined dataset or pre-trained model to get a head start, no need to spend a lot of time training the machine.  
- Create a design document so that it is easier to conclude a report at the end of the project.
- Too much factor to be consider of the project idea:
    - Do elevation of the webcam position affects the recognition
    - Is the road busy enough to have many cars drive by
    - Is the webcam resolution affects the recognition
 
The core of the project revolves around the Machine Learning. If it does not work, need to reconsider the whole project again. 
So take some frames, find dataset and check if it detects cars.

## Week 5 (12<sup>th</sup> November 2019 - 18<sup>th</sup> November 2019)
Yet to find a model that is suitable for the project and no progress has been done. Need more time to look into more dataset 
and object detections so no meeting with the supervisor.

Found a widely used Cars dataset from Stanford with training and testing images:
<https://ai.stanford.edu/~jkrause/cars/car_dataset.html>  
Could do Convolutional Neural Network for cars, need advices from supervisor.

## Week 6 (19<sup>th</sup> November 2019 - 25<sup>th</sup> November 2019)
Code up a detector script to use YOLO/COCO/YOLO-TINY pre-trained model and take some image frames from webcam and do detections.
Output is better than expected while detecting every objects recognized by the model.

Then tried to use the webcam and extract every frame into image and send into the detector function.  
The frame rate is very low due to tensorflow uses CPU instead of GPU.  
Running System:
- Processor: Intel i7-7700K 4.20GHz (8 CPUs)
- Graphic Card: Nvidia GeForce GTX 1080
To get better frame rate and faster processing time, need to somehow use GPU instead.

Spent whole weekend trying to setup Tensorflow GPU.  
Installed Nvidia CUDA toolkit to enable GPU processing and found that tensorflow-gpu doesn't support tensorflow 2.0 yet.  
Reinstalled all packages and libraries and downgraded them so that the tensorflow-gpu supports them.

Finally the tensorflow runs on GPU and the frame rate and processing time dramatically increased.  
[Here is the link to a demo clip of the detector](https://youtu.be/ZLs9EhBChGc)

Note:  
- resnet50_coco_best model has very high accuracy but use more processing time, GPU not powerful enough.
- yolo model has moderate accuracy and moderate processing time, suitable for this project.
- yolo-tiny model has fast processing time but low accuracy, sometimes even cars do not recognize.

## Week 7 (26<sup>th</sup> November 2019 - 2<sup>nd</sup> December 2019)
Did a lot of research on Convolutional Neural Networks. Every research link and references/citations are in the Researches.md.  
Decided to use a pre-trained weights from yolov3 and adapt an existing model script.  
Found ways to use darknet model and convert the already existing yolov3 model to detect just car object.

DarkFlow is a python implementation of YoloV2 using tensorflow but I reckon it works with version 3 too.  
Need to re-train the model to recognise only cars instead of other objects by using the car datasets from Stanford.  
The datasets consist of:
- 8144 training images
- 8041 testing images
- bounding boxes for all images

Problem:
- Bounding boxes data are in .mat format (MatLab) and need to find a way to convert into XML
- Build XML annotation from images and bounding boxes data

## Week 8 (3<sup>rd</sup> December 2019 - 9<sup>th</sup> December 2019)
Tried installing and using Darkflow but most of the stuff had already done by Darkflow using configuration file.  
The Darkflow are easy to use as everything is provided by the repository like labels, datasets, and configs.  
Since I wanted to learn something from this project, I might as well use the ImageAI that I am familiar with and it is 
well documented. Deleted Darkflow net and revert project back to using ImageAI.

Meeting conclusion:
- It is alright that I use ImageAI library preset model and detection.
- Do not overcomplicated the project.
- Try to retrain the ImageAI detection to fewer classes as it now detects over 80 classes.

## Week 9 (10<sup>th</sup> December 2019 - 16<sup>th</sup> December 2019)
Did a little bit of research on how to deploy application onto the cloud server like AWS while taking webcam video feed from it.  
Did not do much stuff, only read some articles about object detections and tracking only to learn that object detection and 
object tracking are two different things.  

What I want for the project is more suitable to implement object tracking than detection as object detection is simply just 
recognise and detect object in a frame but tracking is to identify if the object in the frame is the same as previous frames to 
consider it as the same object. Object tracking opens up a lot of possibilities on data analysis for the data visualization of the project.

Meeting conclusion:
- Last meeting before Christmas.
- Suggested multiple algorithms for object tracking like Kalman filter, Hungarian algorithm and Centroid tracking.
- After finishing tracking, try deploy on cloud servers.

## Week 10 - 13 (17<sup>th</sup> December 2019 - 13<sup>th</sup> January 2020)
Winter exams and Christmas holiday, was out for holiday, no progress on project.  
Did some readings on Kalman filter object tracking and Centroid based object tracking.  
Found a deep learning object tracking library called Simple Online and Realtime Tracking with a Deep Association Metric (DeepSORT).  

## Week 14 (14<sup>th</sup> January 2020 - 22<sup>th</sup> January 2020)
Found multiple ways to detect custom objects without retrain ImageAI models. There are many classes and functions available to filter out 
custom object classes. DeepSORT is a wonderful library but it uses Darkflow object detection library and uses Kalman filter and deep learning 
to track objects by comparing features. The library already implement most of the functionality and is not greatly documented so there are still 
many things I cannot get around with.  

Decided to implement a simple object tracking with OpenCV using centroid based object tracking. The algorithm steps is as follows:
- Take bounding boxes coordinates and compute the center of the bounding box, which identify an object (Centroid).
- Compute Euclidean distance between new bounding boxes and existing objects.
- Update object coordinates to the new bounding boxes representing the object.
- Register the new object when appears and deregister the old object when disappears.