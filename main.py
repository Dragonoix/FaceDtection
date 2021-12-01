# # importing libraries
# import cv2

# # loading cascades   this are feature as open cv library as to use those xml files to detect our motion of our face, smile and eye
# face_cascade = cv2.CascadeClassifier('face.xml')
# eye_cascade = cv2.CascadeClassifier('eye.xml')
# smile_cascade = cv2.CascadeClassifier('smile.xml')


# # make a recognition fucntion which will detect face eye and smile grayimage for black and white, colorimage means to put the color.
# def detect(grayimage, colorimage):
#     faces = face_cascade.detectMultiScale(grayimage,1.3,5)
#     for (x,y,w,h) in faces:

#         # to detect the rectange shape of our face as x and y are the cordinates also w and h are height and width and 255,0,0 as rgb color and 2 is thickness of that rectangle

#         cv2.rectangle(colorimage,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = colorimage[y:y+h,x:x+w]
#         roi_color = colorimage[y:y+h,x:x+w]    # roi is regoin of interest
        
#         # same definitoion for eyes as we defined for face

#         eyes = eye_cascade.detectMultiScale(roi_gray,1.1,22)
#         for (ex,ey,ew,eh) in eyes:
#             cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

#         # same definitoion for smile as we defined for face


#         smiles = smile_cascade.detectMultiScale(roi_gray,1.7,25)
#         for (sx,sy,sw,sh) in smiles:
#             cv2.rectangle(roi_color,(sx,sy), (sx+sw, sy+sh), (0,0,255),2)

#     return colorimage


# # reading real time image 
# video_capture = cv2.VideoCapture(0)  # if using external webcam then use 1 or internal use 0
# while(True):
#     _,colorImg = video_capture.read()
#     gray_img = cv2.cvtColor(colorImg,cv2.COLOR_RGB2GRAY)     # cvt color means convert color 
#     result = detect(gray_img,colorImg)
#     cv2.imshow('Video', result)    # to turn on my camera 

#     # just to exit from loop
#     if cv2.waitKey(1) & 0xff==ord('x'):
#         break
# video_capture.release()      # to detect whatever vatiables we passed from there 
# cv2.destroyAllWindows()      # to destroy everything from windows the video or cam that runs


#import libraries 
import cv2

# loading cascade

face_cascade = cv2.CascadeClassifier('face.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
smile_cascade = cv2.CascadeClassifier('smile.xml')

# Make a recognition fucntion

def detect(grayimage, colorimage):
    face = face_cascade.detectMultiScale(grayimage, 1.3, 5)  # 1.3 as a scaling factor 5 thickness 
    for (x,y,w,h) in face:
        cv2.rectangle(colorimage, (x,y), (x+w, y+h), (255,0,0), 2)   # plotting the segments
        roi_gray = grayimage[y:y+h, x:x+w]   
        roi_color = colorimage[y:y+h, x:x+w]  # y axis as is takes default graph 


        # for eyes

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, eh, ew) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)
        
        #for smiles 

        smile = smile_cascade.detectMultiScale(roi_gray, 1.9, 25)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,0,255), 2)
    return colorimage

# reading real time image

video_capture = cv2.VideoCapture(0)    # 1 for external cameras and 0 for internal cams
while(True):
    _,color_image = video_capture.read()
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2GRAY)   # TO CONVERT THE BLACK AND WHITE TO COLOR FORM
    results = detect(gray_image, color_image)
    cv2.imshow('Video', results)

    # Just to exit from the infinite loop

    if cv2.waitKey(1) & 0xFF==ord('x'):
        break 
video_capture.release()
cv2.destroyAllWindows()




