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