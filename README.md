# Hand-Gesture-Recognition

## This is an application in two parts to help deaf and hard of hearing people to communicate

### First part: Speech to Text
This part of the application listen the speaker and transcribe words to let the deaf people read what the other said

### Second part: Gesture to Speech
This part of the application uses the camera to see the gestures of the deaf people, interpret it and speech for him (or she)

## How to use the code
This code uses the mediapipe library and also uses a model learning that you can calibrate yourself.
Run the Application.py
Use one of three options

![image](https://user-images.githubusercontent.com/89693356/231488904-6c356acc-03ba-4dae-bb6d-6d29ec3c1813.png)

### For the Speech to Text part:
Select 1 in the app
Speak to see the retranscription
Say "quitter" or "fini" or press q to exit

https://user-images.githubusercontent.com/89693356/231491029-2858da3f-21ec-4523-94d7-94156a9a34a7.mp4

### For the Gesture to Speech part:
Select 2 in the app
Do the gestures and the app will speech the word to you

https://user-images.githubusercontent.com/89693356/231490743-ff679da7-eea9-4ef2-ba71-db7014f5d2bc.mp4

### If you want to add gestures:

Type k on your keyboard to enter keypoint mode to train your model
Do your hand gesture and press the corresponding index of this gesture from 0 to 9 and a to e
This will store your keypoints in the "/keypoint.csv" file
Go to "/keypoint_classifier_label.csv" file to give each sign a name
Run the "keyoint_classification.ipynb" to train the model so that you will be able to use it.

Same process with point history to add moving gestures.
