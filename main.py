import cv2 #Importing cv2 for webcam access
import numpy as np
import pyautogui

##To open WebCam
cap = cv2.VideoCapture(0) ## If you are using external webcam use 1

#Setting up colour with rage of RGB
yellow_lower = np.array([22,93,0])
yellow_upper = np.array([45,255,255])
# For finding postion of the object, setting initial postion
prev_y=0

# Creating Loop for Video conversation
while True:
        ret, frame=cap.read() #To read the capture we use read(), we have retrival and frame. We will use Frame
        ####### Masking colour to highlight
        #converting the background frame to grey
        #grey= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame',grey)
        ## Similar way converting to HSV
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Creating Mask from our given color range
        mask=cv2.inRange(hsv,yellow_lower,yellow_upper)
        #Creating 2 variable control and hierarchy to remove noise (false yellow)
        # find controus from the mask and pass method , as external border / outline and chain
        contours, hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #Look through all contours and finding area
        # By running below 3 lines we will get area of yellow in screen
        for c in contours:
            area=cv2.contourArea(c)
            #To remove noise we are adding if condition
            if area > 300:
                # For position of rectange we use cv2.boundingRect(c) and this give 4 things x- horizontal axis, y - vertical axis,w - width,h - height
                x,y,w,h=cv2.boundingRect(c)
                # Drawing for rectangle green
                # initial 2 position x & y
                #then color and 2 for thickness
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                ## Now we are capturing position change of the object
                # For that we are checking by condition
                if y<prev_y:
                    pyautogui.press('space')
                    #print("Its Moving down")
                    # FOr every changes we reset y so to do that prev_y=y
                    prev_y=y
                # this will only draw green line for area more than 300 thats why we are using c there and it can be any shape
                #cv2.drawContours(frame, c,-1,(0,255,0),2)
                #print(area)
        #Draw something, here we use frame where you want to draw for index we use -1 and colour is defined by 3 numbers so (0,255,0) and giving 2 as lines
        #This line will draw all contours, we are commenting this to do specific draw
        #cv2.drawContours(frame, contours,-1,(0,255,0),2)
        #cv2.imshow('Cam See',mask)
        # To display the webacam while reading we use cv2 show 
        cv2.imshow('AutoCam',frame)
        # To stop we use q . it wait for 10 ms and once q typed it will break
        if cv2.waitKey(10)== ord('q'):
            break
# Doing Cleanup
# Now we are releasing from  there
cap.release()
# this will stop windows running
cv2.destroyAllWindows()