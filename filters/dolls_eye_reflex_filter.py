from common.base_auth_filter import BaseAuthFilter
import cv2 as cv
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
import mediapipe as mp
import uuid
from mediapipe.python.solutions.face_mesh import FaceMesh
import math
from exceptions.AuthenticityFailedException import AuthenticityFailedException

LEFT_EYE = 159
RIGHT_EYE = 473

TEST_FILE = "../assets/videoes/VID_20231125_102037.mp4"

TEST_FILE2 = "../assets/videoes/VID_20231124_191002.mp4"
TEST_FILE3 = "../assets/videoes/VID_20231125_102037.mp4"
SlOWED = "../assets/videoes/slowed.mp4"
TEST_FILE4 = "../assets/videoes/VID_20231124_191318.mp4"

class DollsEyeReflexFilter(BaseAuthFilter):

    def __init__(self, video_input) -> None:
        super().__init__(video_input, uuid.uuid4())
        self.face_mesh = FaceMesh(refine_landmarks=True, min_tracking_confidence=0.8)

        #Image resize parameters
        self.image_width = 800
        self.image_height = 600

        #Right eye landmarks
        self.RI_landmark = 468
        self.RE_upper_bound_landmark = 386
        self.RE_lower_bound_landmark = 374
        self.RE_horizontal_bound = 247

        #Left eye landmarks
        self.LI_landmark = 473
        self.LE_upper_bound_landmark = 159
        self.LE_lower_bound_landmark = 145
        self.LE_horizontal_bound = 467

    def analyze_left_eye(self, landmarks, iris_landmarks, frame):
            
        #Left eye lower and upper bounds coordinates
        lux = int(landmarks.landmark[self.LE_upper_bound_landmark].x *self.image_width)
        luy = int(landmarks.landmark[self.LE_upper_bound_landmark].y *self.image_height)
        llx = int(landmarks.landmark[self.LE_lower_bound_landmark].x *self.image_width)
        lly = int(landmarks.landmark[self.LE_lower_bound_landmark].y *self.image_height)


        #Left iris position
        lx = int(iris_landmarks.x * self.image_width)
        ly = int(iris_landmarks.y * self.image_height)


        #Horizontal bound
        left_horizontal_eye_bound = landmarks.landmark[self.LE_horizontal_bound]
        px = int(left_horizontal_eye_bound.x*self.image_width)
        py = int(left_horizontal_eye_bound.y*self.image_height)

        distance_between_horizontal_control_iris = math.sqrt(math.pow((lx-px),2) + math.pow((ly-py),2))

        #Detecting iris
        cv.circle(frame, (lx, ly),  1, (0,0,255), 1)

        #Left eye center line
        cv.line(frame,(lux, luy),(llx, lly), (0,255,0), 1)

        #Distance between left eye horizontal bound and iris 
        cv.circle(frame, (px, py), 1, (0,255,255), 1)
        cv.line(frame,(px, py), (lx, ly), (0,255,255), 1)

        return distance_between_horizontal_control_iris

    def analyze_right_eye(self, landmarks, iris_landmarks, frame):
        
        #Right eye upper and lower bounds coordinates
        rux = int(landmarks.landmark[self.RE_upper_bound_landmark].x *self.image_width)
        ruy = int(landmarks.landmark[self.RE_upper_bound_landmark].y *self.image_height)
        rlx = int(landmarks.landmark[self.RE_lower_bound_landmark].x *self.image_width)
        rly = int(landmarks.landmark[self.RE_lower_bound_landmark].y *self.image_height)

        #Right iris position
        rx = int(iris_landmarks.x * self.image_width)
        ry = int(iris_landmarks.y * self.image_height)

        #Horizontal bound
        right_horizontal_eye_bound = landmarks.landmark[self.RE_horizontal_bound]
        px = int(right_horizontal_eye_bound.x * self.image_width)
        py = int(right_horizontal_eye_bound.y * self.image_height)
        distance_between_horizontal_control_iris = math.sqrt(math.pow((rx-px),2) + math.pow((ry-py),2))

        #Detecting iris
        cv.circle(frame, (rx, ry),  1, (0,0,255), 1)

        #Right eye center line
        cv.line(frame,(rux, ruy),(rlx, rly), (0,255,0), 1)


        #Distance between right eye horizontal bound and iris 
        cv.circle(frame, (px, py), 1, (0,255,255), 1)
        cv.line(frame,(px, py), (rx, ry), (0,255,255), 1)

        return distance_between_horizontal_control_iris
       
      
    
    def run(self):
        cap =  cv.VideoCapture(self.video_input)

        if not cap.isOpened():
            print("Cannot open camera")
        left_eye_values = []
        right_eye_values = []
        l_maximum = 0
        l_minimum  = 0
        r_maximum  = 0
        r_minimum = 0
        left_threshold = 0
        right_threshold = 0

        while cap.isOpened():
        
            ret, frame = cap.read()
            if not ret:
                print("Nincs már több frame")
                break
            frame = cv.resize(frame, (800, 600))
            
            result = self.face_mesh.process(frame)
            
            try:
                for facial_landmarks in result.multi_face_landmarks:
                
                    left_iris = facial_landmarks.landmark[self.LI_landmark]
                    right_iris = facial_landmarks.landmark[self.RI_landmark]
                   
                    left_eye_result = self.analyze_left_eye(facial_landmarks, left_iris, frame)
                    right_eye_result = self.analyze_right_eye(facial_landmarks, right_iris, frame)
                    left_threshold = left_eye_result
                    right_threshold = right_eye_result
                    left_eye_values.append(left_eye_result)
                    right_eye_values.append(right_eye_result)
            except Exception as ex:
                pass
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        cap.release()

    
        l_maximum = max(left_eye_values)
        l_minimum = min(left_eye_values)

        r_maximum = max(right_eye_values)
        r_minimum = min(right_eye_values)

        print(right_threshold, left_threshold)
        print(r_maximum, r_minimum)
        print(l_maximum, l_minimum)
        

        if (abs(l_maximum-l_minimum) < left_threshold or abs(r_maximum-r_minimum) < right_threshold):
            raise AuthenticityFailedException("Eye is not moving!")
       
        cv.destroyAllWindows()



if __name__ == "__main__":
    dolls_eye_reflex_filter = DollsEyeReflexFilter(TEST_FILE3)
    try:
        dolls_eye_reflex_filter.run()
    except AuthenticityFailedException as ex:
        print("Threshold reached, possible AI because dolls eye reflex absence!")

  