from flask import Flask, render_template, Response
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

web = Flask(__name__)    #Initializing Flask
camera = cv2.VideoCapture(0)   #to get Webcam feed into the variable camera
detector = HandDetector(maxHands=1)    #Uses prebuilt function from CV Zone to detect Hands
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")   #Classifier to classify given input

offset = 20
imgSize = 300

folder = "Data/C"
counter = 0

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Calm Down", "Hello", "Love", "Stand", "Thumbs Up", "Where"]
#Labels which are going to be shown on on the User Output screen
@web.route('/') #making the homepage/indexpage of our website
def index(): #purpose is to render the index.html file
    return render_template('index.html')

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            while True:
                success, img = camera.read()  #Input from webcam is read
                imgOutput = img.copy()        #it is copied in imgOutput to get output without skeletal points
                hands, img = detector.findHands(img)  #to get detect hands
                if hands:
                    hand = hands[0]
                    x, y, w, h = hand['bbox']     #assigning bounding box co-ord

                    imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255     #for even img(square)
                    imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

                    imgCropShape = imgCrop.shape

                    # adjusting the cropped img in white img
                    aspectRatio = h / w

                    #if image is vertical
                    if aspectRatio > 1:     #for height of the bounding box
                        k = imgSize / h
                        wCal = math.ceil(k * w)  #Math.ceil() always rounds up and returns the smaller integer greater than or equal to a given number
                        imgResize = cv2.resize(imgCrop, (wCal, imgSize)) #cv2.resize() function is that the tuple passed for determining the size of the new image
                        imgResizeShape = imgResize.shape
                        wGap = math.ceil((imgSize - wCal) / 2)     #adjusting img in the centre of the bounding box
                        imgWhite[:, wGap:wCal + wGap] = imgResize  #for putting the image in white background
                        prediction, index = classifier.getPrediction(imgWhite, draw=False) #getting the prediction
                        print(prediction, index)

                    #if image is horizontal
                    else:               #for width of the bounding box
                        k = imgSize / w
                        hCal = math.ceil(k * h)
                        imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                        imgResizeShape = imgResize.shape
                        hGap = math.ceil((imgSize - hCal) / 2)
                        imgWhite[hGap:hCal + hGap, :] = imgResize
                        prediction, index = classifier.getPrediction(imgWhite, draw=False)

                   # cv2.rectangle(imgOutput, (x-offset , y - offset -50),
                       #           (x - offset + 270, y - offset - 50+50), (255, 0, 255), cv2.FILLED)

                    #text settings
                    cv2.putText(imgOutput, labels[index], (x-offset, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.3, (255,78,63), #color values in BGR
                                3)

                    #bounding box settings
                    cv2.rectangle(imgOutput, (x - offset, y - offset),
                                  (x + w + offset, y + h + offset), (70, 252, 255), 6)

                    ret, buffer = cv2.imencode('.jpg', imgOutput)   #converting into jpeg format
                    frame = buffer.tobytes()    #converting into bytes
                    yield (b'--frame\r\n'       #creating a html render template
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                    #We will be displaying a frame with some para (\r\n). the content type of the frame is image
                    #then display the frame

@web.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame') #mimetype Descrbes what kind of response html will be receiving
if __name__=='__main__': #if name=main then run web
    web.run(debug=True)  #debug: when we make any changes in our code, we only need to refresh the webpage and not reopen the server


