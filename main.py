import cv2 #Importing cv2 for webcam access

##To open WebCam
cap = cv2.VideoCapture(0) ## If you are using external webcam use 1

# Creating Loop for Video conversation
while True:
        ret, frame=cap.read() #To read the capture we use read(), we have retrival and frame. We will use Frame
        # To display the webacam while reading we use cv2 show 
        cv2.imshow('frame',frame)
        # To stop we use q . it wait for 10 ms and once q typed it will break
        if cv2.waitKey(10)== ord('q'):
            break
# Doing Cleanup
# Now we are releasing from  there
cap.release()
# this will stop windows running
cv2.destroyAllWindows()