from scipy.spatial import distance
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from imutils import face_utils
import imutils
import dlib
import cv2
import os
import RPi.GPIO as IO  

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear
print("\nHello")
thresh = 0.25
frame_check = 10
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("/home/pi/Desktop/shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap= cv2.VideoCapture(-1)
flag=0

duration = 0.85
freq = 2200

IO.setwarnings(False)
IO.setmode (IO.BOARD)     
IO.setup(40,IO.OUT)
IO.cleanup()

while True:
    ret, frame=cap.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    for subject in subjects:
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)#converting to NumPy Array
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        if ear < thresh:
            flag += 1
            print (flag,frame_check)
            if flag >= frame_check:
                cv2.putText(frame, "****************ALERT!****************", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "****************ALERT!****************", (10,325),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                print ("Drowsy")
                os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration,freq))
                IO.setmode (IO.BOARD)
                IO.setup(40,IO.OUT)
                IO.output(40,1)
                time.sleep(0.1)
                IO.cleanup()
                time.sleep(0.1)


                IO.setmode (IO.BOARD)
                IO.setup(40,IO.OUT)
                IO.output(40,1)
                time.sleep(0.1)
                IO.cleanup()
                time.sleep(0.1)
        else:
            flag = 0
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
cap.stop()
IO.cleanup()