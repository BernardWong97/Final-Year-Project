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

Decided to implement a simple object tracking with OpenCV using centroid based object tracking by referencing [PyImageSearch's Algorithm](https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/).  
The algorithm steps is as follows:
- Take bounding boxes coordinates and compute the center of the bounding box, which identify an object (Centroid).
- Compute Euclidean distance between new bounding boxes and existing objects.
- Update object coordinates to the new bounding boxes representing the object.
- Register the new object when appears and deregister the old object when disappears.

## Week 15 (23<sup>rd</sup> January 2020 - 29<sup>th</sup> January 2020)
General Data Protection Regulation (GDPR) came into my mind and I am worried that the legislation may affect the project regarding taking live video of vehicles and pedestrian without their consent. 
I will ask the supervisor regarding the GDPR legislation for some advices.  

Tried to implement centroid object tracking and output of the implementation has a lot of issues:
- Object ID changes when collides with other bounding boxes.
- Centroid still floats around even after the object disappeared from the view.
- Losses of detection on the same object may or may not recognized as a new object.

Meeting conclusion:  
- Supervisor concerns about this project have a direct relation of the GDPR legislation, advising to pause the project on live streaming taking footage 
of the public domain and have a look into the legislation to see whether it is allowed to do so.
- Just the centroid tracking is not stable enough to identify the object whether is the same one from the previous frames. Need to use Kalman filter to 
estimate the possibility of the next bounding box position to track it efficiently.
- Try to take a break from the research part of the project (Object tracking) and give some time into preparing for application build and deployment like web application.

## Week 16 (30<sup>th</sup> January 2020 - 5<sup>th</sup> February 2020)
Contacted some lecturers and Data Protection Officers from the campus for advices regarding the GDPR had any impact to my project. They want to see if my live video feed is doing the following:
- Is the webcam capturing any identifiable personal data (identify individuals and/or car registration plates)?
- Does this add any value to your project or is your requirement simply for object detection/tracking without necessarily identifying the individuals/objects?
- How far zoomed is the webcam (is it just capturing road traffic? Is it capturing images of individuals entering the residence)?

Did extensive researches on Kalman filter and could not really understand how to implement it into my project. There are limited resource online regarding 
predict next position of bounding box using the Kalman filter algorithm. This [blog](https://medium.com/@jaems33/understanding-kalman-filters-with-python-2310e87b8f48) gave a very 
good insight on how Kalman filter works and implementation, but I am still struggling on how to adapt it into my project.

## Week 17 (6<sup>th</sup> February 2020 - 13<sup>th</sup> February 2020)
Giving myself a breather, pause the research and much more difficult part of the project like implementing Kalman Filter algorithm and switch the project progress to deployment. 
Set up Flask server and try stream data onto the serving Flask app.  
Installed React and Flask and tried the basic hello world application see if it works. Decided to branch off React from the master branch.  
The goal is to set up an environment where Reactjs web-app can take data from Flask API and serve onto the website (React frontend/ Flask backend). 
An idea came up that the React web-app can have different components for users to choose, as in:
- Live streaming object tracking and data analysis
- Upload video and apply object tracking and data analysis
- Upload photo and apply object detection and data analysis

Did a little tweaking on the centroid tracking so that there are no lingering centroid when bounding box disappears but the object is still registered as an existing object before. 
The inconsistency of the object tracking like flickering and constantly changing size of bounding box is out of my control, only can minimize the tracking inconsistency from tracking algorithms.  

Thoughts about application deployment, this application must use a mid to high end GPU for good performance. 
Google Cloud machines offers GPU but does not rent GPU machines for free credit accounts. Leave the deployment until the application is completely developed.

Goal for the next few weeks:
- Live stream video from Flask to React
- Do data analysis (graphs, charts, summaries)
- Start writing dissertation/ report

## Week 18 (14<sup>th</sup> February 2020 - 19<sup>th</sup> February 2020)
For some reason, the Flask cannot even stream frames from the webcam to the server. 
The problem is from stuck in infinite while loop and repeatedly initialize everything, including webcam and detector model. 
After setting up scripts into classes and implement OOP design, the live video stream of the webcam (frames) are successfully sent to the server 
and displayed to port 5000.

Tried to port forwarding router and firewalls to access from outside the local network so that I can run and display in college for my supervisor but it seems 
that I was not suppose to do that. The only option is to deploy it onto the cloud and accessing the website that is on the cloud server.

After fixing sending webcam feed to the Flask server, I tried to send processed frames to it but failed as the application could not find the model file.  
In the meantime, I displayed the object classes/names onto the frames inside the bounding box with their object identifier for future data analysis usage.

Meeting conclusion:
- To show that this application concerns about GDPR legislation, supervisor and Data Protection Officer recommend do a Gaussian Blur in the bounding box to 
blur out the pedestrians, vehicles and find a way to cancel out the neighbor's front yard after the processing operation.
- Need to modify current work directory or use os pathing in order for the application to find the modules and folders.
- Do all the processing and heavy load work on local machine but only send simplify data to the server/API so that the server can deploy onto cloud without many consideration like GPU requirement.

## Week 19 (20<sup>th</sup> February 2020 - 26<sup>th</sup> February 2020)
After changing the working directory and file pathing, the model successfully works and the application also successfully send processed video frames to 
the listening port. Refactor code and migrate video capture to flask app script rather than the video processing class. I also resized and cropped the video frames to remove the neighbour's front 
yard because of GDPR concern and increase detection accuracy.

GDPR concern:
- Neighbour's front yard is showing and need to find a way to censor it.
- In every bounding box, blur the object inside the boxes.

Structure of the application is not yet determine. For now, the application is collecting frames from the webcam and process object tracking in every frame of the video feed 
then send as a response to the Flask server. Flask then display the video feed to the website of that particular port. Issue here is the serving end point is streaming the video 
frames to the website and it is hogging up the request. Need to find a way to also stream the meta-data of the processed frames for data analysis.

Meeting conclusion:
- Set aside everything and try to apply blurring and censoring bounding boxes and neighbour's front yard (Revert zoom).
- Object ID is incrementing regardless of object types (first car has id=1, first person came in will be id=2, need to be car 1, person 1)
- Advised by supervisor, do processing and manipulating stuff on local machine and send meta-data to cloud for front-end.
- Figure out how to transfer streaming data to static website.

## Week 20 (27<sup>th</sup> February 2020 - 4<sup>th</sup> March 2020)
Applied Gaussian blur in all the detected object's bounding box so when a person or car is detected, they are blurred. I thought of multiple 
ways to censoring neighbour's front yard:
- Applying Gaussian blur also.
- Blacken out by masking.
- Mosaic (pixelate) the region of interest.

