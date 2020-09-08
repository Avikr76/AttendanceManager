
import cv2,os
# import numpy as np
import pickle
from datetime import datetime
import pandas as pd


import cv2, os
import numpy as np
from PIL import Image
import pyttsx3

#pip install pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak("Welcome To Face Recognition")


now=datetime.now()
print(now)
def markAttendance(name):
    with open('attendence.csv', 'r+') as f:
        mylist = f.readlines()
        # print(date)
        # print(mylist)
        namelist = []
        for line in mylist:
            entry = line.split(',')
            # print(entry)
            # print(entry[2])
            namelist.append(entry[0])
            # print(ddstring)
            # qprint(entry[1])
        if name not in namelist:
            now = datetime.now()
            ddstring = now.strftime('%d/%m/%Y')
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{ddstring},{dtstring}')

            f = 'attendence.csv'
            convert(f)


def convert(file):
    df = pd.read_csv(file)
    df.to_excel('Attendence.xlsx', sheet_name='Sheet1')


face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('data/haarcascade_smile.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

img = cv2.VideoCapture(0)
img.set(3, 1700)
img.set(4, 1700)
img.set(10, 150)

while (True):
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 5)
    
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        
        # Recogniser
        id_, conf = recognizer.predict(roi_gray)
        
        if conf >= 45:  # and conf<=85:
            print(id_)
          
            print(labels[id_])
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            markAttendance(name)
            
        # img_item = "6.png"
        # img_item1="my_img1.png"
        # cv2.imwrite(img_item,roi_gray)
        # cv2.imwrite(img_item,roi_color)

        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        subitems = smile_cascade.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in subitems:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

img.release()
cv2.destroyAllWindows()
