from common.base_auth_filter import BaseAuthFilter
import keras
import tensorflow as tf
import numpy as np
import cv2
import os
import base64
import pybase64
import random

from model.deep_fake_model import DeepFakeDetectionModel




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



class DeepFakeDetectionFilter(BaseAuthFilter):


    def __init__(self, video_input) -> None:
        super().__init__(video_input)




    def run(self, video_input):
       
        video = cv2.VideoCapture(files[0])
        fps = video.get(cv2.CAP_PROP_FPS)
        totalFrames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        counter = 0
        for times in range(0, int(totalFrames*0.05)):
            randomFrameNumber=random.randint(0, totalFrames)
            video.set(cv2.CAP_PROP_POS_FRAMES, randomFrameNumber)
            ret, frame = video.read()
            cv2.imwrite("img{counter}.png".format(counter = counter), frame)
           
        
            model = DeepFakeDetectionModel("img{counter}.png".format(counter = counter),)
            model.predict()
            counter+=1



if __name__ == "__main__":
    deep_fake_detection_filter = DeepFakeDetectionFilter(files[0])
   
    deep_fake_detection_filter.run(files[0])