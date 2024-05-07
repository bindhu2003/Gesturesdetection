#modules imported for project
import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector
import math
import time
 
 #Intialize the video capture
cap=cv2.VideoCapture(0)

# Initialize PoseDetector with specified confidence thresholds
pd =PoseDetector(trackCon=0.70,detectionCon=0.70)

#functions for different cricket signals

#function to print "OUT"
def OUT():
    cv2.putText(img,str("OUT"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#function to print "6"
def SIXER():
    cv2.putText(img,str("6"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#functiono to print "4"
def FOUR():
    cv2.putText(img,str("4"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#function to print "WIDE"
def WIDE():
    cv2.putText(img,str("WIDE"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#function to print "TIME_OUT"
def TIME_OUT():
    cv2.putText(img,str("TIME_OUT"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)


#function to calcualte angles between specific points and recognize cricket signals
def an(lmlist,p1,p2,p3,p4,p5,p6,drawpoints):
    if len(lmlist)!=0:
        point1=lmlist[p1]
        point2=lmlist[p2]
        point3=lmlist[p3]
        point4=lmlist[p4]
        point5=lmlist[p5]
        point6=lmlist[p6]
        
        x1,y1=point1[1:-1]
        x2,y2=point2[1:-1]
        x3,y3=point3[1:-1]
        x4,y4=point4[1:-1]
        x5,y5=point5[1:-1]
        x6,y6=point6[1:-1]

        if drawpoints==True:
            cv2.circle(img,(x1,y1),10,(255,0,255),5)
            cv2.circle(img,(x1,y1),10,(0,255,0),5)
            
            cv2.circle(img,(x2,y2),10,(255,0,255),5)
            cv2.circle(img,(x2,y2),10,(0,255,0),5)

            cv2.circle(img,(x3,y3),10,(255,0,255),5)
            cv2.circle(img,(x3,y3),10,(0,255,0),5)

            cv2.circle(img,(x4,y4),10,(255,0,255),5)
            cv2.circle(img,(x4,y4),10,(0,255,0),5)

            cv2.circle(img,(x5,y5),10,(255,0,255),5)
            cv2.circle(img,(x5,y5),10,(0,255,0),5)

            cv2.circle(img,(x6,y6),10,(255,0,255),5)
            cv2.circle(img,(x6,y6),10,(0,255,0),5)

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),6)
            cv2.line(img,(x2,y2),(x3,y3),(0,0,255),6)
            
            cv2.line(img,(x4,y4),(x5,y5),(0,0,255),6)
            cv2.line(img,(x5,y5),(x6,y6),(0,0,255),6)

            #calculate angles between points
            angle1=math.degrees(math.atan2(x1,x2)-math.atan2(y1,y2))
            angle2=math.degrees(math.atan2(x2,x3)-math.atan2(y2,y3))
            angle3=math.degrees(math.atan2(x4,x5)-math.atan2(y4,y5))
            angle4=math.degrees(math.atan2(x5,x6)-math.atan2(y5,y6))

            #print angles if required
            print(angle1,angle2,angle3,angle4)

            #If angles match predefined criteria, recognize specific cricket signal
            #call corresponding cricket signal function and display text on screen
            if angle1>9 and angle1<13 and angle2>-8 and angle2<-5 and angle3>-16 and angle3<-13 and angle4>-21 and angle4<-19:
                SIXER()

            elif angle1>20 and angle1<40 and angle2>4 and angle2<10 and angle3>-20 and angle3<-10 and angle4>-23 and angle4<-16:
                SIXER() 
            elif angle1>4 and angle1<8 and angle2>-2 and angle2<1 and angle3>-6 and angle3<-3 and angle4>-7 and angle4<-2:
                TIME_OUT() 
            elif angle1>10 and angle1<28 and angle2>5 and angle2<10 and angle3>-19 and angle3<-10 and angle4>-14 and angle4<-3:
                TIME_OUT()
            elif angle1>-1 and angle1<1 and angle2>-10 and angle2<-6:
                FOUR()
            elif angle1>-80 and angle1<-40 and angle2>-40 and angle2<-20:
               FOUR()
            elif angle1>-8 and angle1<-6 and angle2>-11 and angle2<-9 and angle3>1 and angle3<3 and angle4>-4 and angle4<-2:
                WIDE()
            elif angle1>-110 and angle1<-50 and angle2>-36 and angle2<-20 and angle3>-12 and angle3<-4 and angle4>-10 and angle4<-5:
                WIDE()
            elif angle1>-10 and angle1<0 and angle2>-10  and angle2<-5 and angle3>-10 and angle3<-1 and angle4>-8 and angle4<0:
                WIDE()
            elif angle1>11 and angle1<15 and angle2>-3 and angle2<3:
                OUT()
            elif angle1>17 and angle1<32 and angle2>3 and angle2<12:
                OUT()


#Main loop to capture video frames and process yoga poses
start_time=time.time()
while 1:
    ret,img=cap.read()
    if not ret:
        cap=cv2.VideoCapture(0)
        continue

    #size of output screen
    img=cv2.resize(img,(1400,700))

    #Detect poses and find landmarks
    pd.findPose(img,draw=0)
    lmlist,bbox=pd.findPosition(img, draw=0,bboxWithHands=0)
    
    #Call the angles function to determine yoga pose and display it on image
    an(lmlist, 16, 14, 12, 11, 13, 15,drawpoints=1)

    # Get the current time
    current_time = time.time()

    # Check if 40 seconds have passed, if yes, break out of the loop
    if current_time - start_time > 40:
        break
    cv2.imshow('output',img)
    cv2.waitKey(40)