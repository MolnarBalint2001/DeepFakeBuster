from common.base_auth_filter import BaseAuthFilter
import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
import mediapipe as mp



class DollsEyeReflexFilter(BaseAuthFilter):

    def __init__(self, video_input) -> None:
        super().__init__(video_input)
        self.mp_drawing = mp.solutions.drawing.utils
        self.mp_holisitc = mp.solutions.holistic
    
    def run(self):
        pass