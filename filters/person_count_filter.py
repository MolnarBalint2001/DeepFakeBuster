from common.base_auth_filter import BaseAuthFilter
import mediapipe as mp
import cv2
import numpy as np
from exceptions.AuthenticityFailedException import AuthenticityFailedException

FILE_PATH = "../assets/videoes/VID_20231124_191002.mp4"


files = [
    "../assets/videoes/VID_20231124_191002.mp4",
    "../assets/videoes/VID_20231124_191025.mp4",
    "../assets/videoes/VID_20231124_191034.mp4",
    "../assets/videoes/VID_20231124_191044.mp4",
    "../assets/videoes/VID_20231124_191059.mp4",
    "../assets/videoes/VID_20231124_191150.mp4",
    "../assets/videoes/VID_20231124_191202.mp4",
    "../assets/videoes/VID_20231124_191208.mp4",
    "../assets/videoes/VID_20231124_191232.mp4",
    "../assets/videoes/VID_20231124_191304.mp4",
    "../assets/videoes/VID_20231124_191318.mp4",
    "../assets/videoes/VID_20231124_191418.mp4",
    "../assets/videoes/VID_20231124_191435.mp4",
]


class PersonCountFilter(BaseAuthFilter):

    def __init__(self, video_input) -> None:
        super().__init__(video_input)
        self.face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.2)
        self.holistic =  mp.solutions.holistic.Holistic(min_detection_confidence=0.2)
        self.mp_drawing = mp.solutions.drawing_utils
        self.results = []

    def run(self, file_path):
        cap = cv2.VideoCapture(file_path)
        
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            

            result = self.face_detection.process(frame)
            if result.detections == None:
                raise AuthenticityFailedException("Multiple person recognized on the video!")
            if len(result.detections) > 1:
                raise AuthenticityFailedException("Multiple person recognized on the video!")
        cap.release()
        cv2.destroyAllWindows()
    
        
if __name__ == "__main__":
    person_count_filter = PersonCountFilter(FILE_PATH)

    for file in files:
        try:
            result = person_count_filter.run(file)
            print("+ One person recognized only!")

        except AuthenticityFailedException as ex:
            print("- More person recognized")
      
       
      