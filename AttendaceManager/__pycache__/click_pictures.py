# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:42:56 2020

@author: Rituraj
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:57:38 2020

@author: Rituraj
"""
from tkinter import *
import cv2
#import name
import os

print("hello7")

root = Tk()

e = Entry(root, width = 50)
e.pack()
e.insert(0,"")
def myClick():

    print(e.get())
    return "ded"

print("hello6")
myButton = Button(root, text="Enter", command = myClick)
myButton.pack()
root.mainloop()
na = myClick()
print("hello8")
path = 'C:\\Users\\Abhinav\\Desktop\\Images'
os.chdir(path)
new = na
os.mkdir(new)
count=0
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

while True:
    success,img = cap.read()
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("C:/Users/Abhinav/Desktop/Images/"+new+"/"+str(count)+".jpg",img)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,0),2)
        cv2.imshow("Image",img)
        cv2.waitKey(0)
        count+=1

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()
