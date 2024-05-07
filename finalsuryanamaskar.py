#modules imported for project
import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector
import math
import time

#Intialize the video capture and PoseDetector objects
cap=cv2.VideoCapture(0)
pd=PoseDetector(trackCon=0.40,detectionCon=0.40)

#functions for printing asanas

#function to print pranaam asana
def PRANAAM_ASANA():
    cv2.putText(img,str("PRANAAM ASANA"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#function to print hastha uttasana
def HASTHA_UTTASANA():
    cv2.putText(img,str("HASTHA UTTASANA"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#function to print hasthapadasana
def HASTAPADASANA():
    cv2.putText(img,str("HASTAPADASANA"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#function to print ashwa sanchalan asana
def ASHWA_SANCHALAN_ASANA():
    cv2.putText(img,str("ASHWA SANCHALAN ASANA"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#function to print dandasana
def DANDASANA():
    cv2.putText(img,str("DANDASANA"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)

#function to print parvatasana
def PARVATASANA():
    cv2.putText(img,str("PARVATASANA"),(40,160),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),10)


#function to calcualte angles between specific points and recognize yoga poses 
def angles(lmlist,p1,p2,p3,p4,p5,p6,p7,p8,drawpoints):
    if len(lmlist)!=0:
        #extract coordinates of specific points
        point1=lmlist[p1]
        point2=lmlist[p2]
        point3=lmlist[p3]
        point4=lmlist[p4]
        point5=lmlist[p5]
        point6=lmlist[p6]
        point7=lmlist[p7]
        point8=lmlist[p8]
        
        x1,y1=point1[1:-1]
        x2,y2=point2[1:-1]
        x3,y3=point3[1:-1]
        x4,y4=point4[1:-1]
        x5,y5=point5[1:-1]
        x6,y6=point6[1:-1]
        x7,y7=point7[1:-1]
        x8,y8=point8[1:-1]

        if drawpoints==True:
            cv2.circle(img,(x1,y1),5,(255,0,255),5)
            cv2.circle(img,(x1,y1),5,(0,255,255),0)

            cv2.circle(img,(x2,y2),5,(255,0,255),5)
            cv2.circle(img,(x2,y2),5,(0,255,255),0)

            cv2.circle(img,(x3,y3),5,(255,0,255),5)
            cv2.circle(img,(x3,y3),5,(0,255,255),0)

            cv2.circle(img,(x4,y4),5,(255,0,255),5)
            cv2.circle(img,(x4,y4),5,(0,255,255),0)

            cv2.circle(img,(x5,y5),5,(255,0,255),5)
            cv2.circle(img,(x5,y5),5,(0,255,255),0)

            cv2.circle(img,(x6,y6),5,(255,0,255),5)
            cv2.circle(img,(x6,y6),5,(0,255,255),0)

            cv2.circle(img,(x7,y7),5,(255,0,255),5)
            cv2.circle(img,(x7,y7),5,(0,255,255),0)

            cv2.circle(img,(x8,y8),5,(255,0,255),5)
            cv2.circle(img,(x8,y8),5,(0,255,255),0)


            #calculate angles between points
            angle1=math.degrees(math.atan2(x1,x2)-math.atan2(y1,y2))
            angle2=math.degrees(math.atan2(x2,x3)-math.atan2(y2,y3))
            angle3=math.degrees(math.atan2(x3,x4)-math.atan2(y3,y4))
            angle4=math.degrees(math.atan2(x4,x5)-math.atan2(y4,y5))
            angle5=math.degrees(math.atan2(x5,x6)-math.atan2(y5,y6))
            angle6=math.degrees(math.atan2(x6,x7)-math.atan2(y6,y7))
            angle7=math.degrees(math.atan2(x7,x8)-math.atan2(y7,y8))
            angle8=math.degrees(math.atan2(x3,x8)-math.atan2(y3,y8))

            #print angles if required
            print(angle1,angle2,angle3,angle4,angle5,angle6,angle7,angle8)

            #If angles match predefined criteria, recognize specific yoga pose
            #call corresponding yoga pose function and display text on screen
            if angle1>2 and angle1<5 and angle2>2 and angle2<8 and angle3>-2 and angle3<0 and angle4>-2 and angle4<2 and angle5>6 and angle5<10 and angle6>3 and angle6<6 and angle7>3 and angle7<6 and angle8>14 and angle8<17:
                PRANAAM_ASANA()

            elif angle1>3 and angle1<8 and angle2>10 and angle2<20 and angle3>-5 and angle3<2 and angle4>-4 and angle4<1 and angle5>12 and angle5<18 and angle6>9 and angle6<14 and angle7>5 and angle7<10 and angle8>14 and angle8<28:
                PRANAAM_ASANA()

            elif angle1>1 and angle1<8 and angle2>-10 and angle2<-5 and angle3>-11 and angle3<-8 and angle4>-4 and angle4<-1 and angle5>22 and angle5<32 and angle6>4 and angle6<8 and angle7>3 and angle7<5 and angle8>24 and angle8<28:
                HASTHA_UTTASANA()
            
            elif angle1>2 and angle1<10 and angle2>-18 and angle2<-10 and angle3>-26 and angle3<-16 and angle4>-10 and angle4<0 and angle5>36 and angle5<52 and angle6>8 and angle6<12 and angle7>4 and angle7<8 and angle8>32 and angle8<44:
                HASTHA_UTTASANA()

            elif angle1>-1 and angle1<1 and angle2>2 and angle2<4 and angle3>-1 and angle3<3 and angle4>-1 and angle4<1 and angle5>-14 and angle5<-9 and angle6>5 and angle6<7 and angle7>2 and angle7<6 and angle8>-2 and angle8<2:
                HASTAPADASANA()

            elif angle1>-10 and angle1<0 and angle2>2 and angle2<10 and angle3>1 and angle3<10 and angle4>-2 and angle4<2 and angle5>-28 and angle5<-16 and angle6>8 and angle6<12 and angle7>5 and angle7<10 and angle8>2 and angle8<12:
                HASTAPADASANA()

            elif angle1>2 and angle1<5 and angle2>7 and angle2<10 and angle3>5 and angle3<7 and angle4>0 and angle4<2 and angle5>-13 and angle5<-10 and angle6>-2 and angle6<0 and angle7>-8 and angle7<-5 and angle8>-15 and angle8<-9:
                ASHWA_SANCHALAN_ASANA()

            elif angle1>-2 and angle1<2 and angle2>4 and angle3>4 and angle3<8 and angle4>0 and angle4<4 and angle5>-22 and angle5<-14 and angle6>-2 and angle6<2 and angle7>-10 and angle7<-2 and angle8>-20 and angle8<-14:
                ASHWA_SANCHALAN_ASANA()  

            elif angle1>-3 and angle1<0 and angle2>1 and angle2<7 and angle3>6 and angle3<8 and angle4>2 and angle4<8 and angle5>-29 and angle5<-26 and angle6>2 and angle6<6 and angle7>2 and angle7<6 and angle8>-11 and angle8<-8:
                DANDASANA()

            elif angle1>-4 and angle1<4 and angle2>2 and angle2<8 and angle3>2 and angle3<6 and angle4>0 and angle4<4 and angle5>-20 and angle5<-14 and angle6>-8 and angle6<-4 and angle7>-8 and angle7<-4 and angle8>-20 and angle8<-14:
                DANDASANA()   
                
            elif angle1>-3 and angle1<0 and angle2>1 and angle2<8 and angle3>6 and angle3<9 and angle4>0 and angle4<4 and angle5>-39 and angle5<-37 and angle6>8 and angle6<11 and angle7>4 and angle7<7 and angle8>-14 and angle8<-12:
                PARVATASANA()
            
            elif angle1>-8 and angle1<0 and angle2>2 and angle2<10 and angle3>4 and angle3<10 and angle4>0 and angle4<4 and angle5>-36 and angle5<-26 and angle6>4 and angle6<10 and angle7>0 and angle7<5 and angle8>-16 and angle8<-10:
                PARVATASANA()
            
            elif angle1>-5 and angle1<-1 and angle2>2 and angle2<8 and angle3>4 and angle3<8 and angle4>-2 and angle4<4 and angle5>-20 and angle5<-15 and angle6>0 and angle6<10 and angle7>-10 and angle7<0 and angle8>-10 and angle8<-2:
                ASHWA_SANCHALAN_ASANA()

#Main loop to capture video frames and process yoga poses
start_time=time.time()
while 1:
    ret,img =cap.read()
    if not ret:
        cap=cv2.VideoCapture(0)
        continue

    #size of output screen
    img=cv2.resize(img,(1400,700))

    #Detect poses and find landmarks
    pd.findPose(img,draw=0) 
    lmlist ,bbox = pd.findPosition(img ,draw=0,bboxWithHands=0)

    #Call the angles function to determine yoga pose and display it on image
    angles(lmlist,0,11,13,15,17,23,25,27,drawpoints=1)
    current_time=time.time()
    if current_time-start_time>50:
        break

    #display the processed video frame
    cv2.imshow('video output',img)
    cv2.waitKey(40)