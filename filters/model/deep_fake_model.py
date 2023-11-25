
from transformers import pipeline



class DeepFakeDetectionModel:


    def __init__(self, image_input) -> None:
        self.image_input = image_input




    def load_pretrained_model(self):
        pretrained_model = pipeline("image-classification", model="joyc360/deepfakes")
        return pretrained_model
    

    def predict(self):
        pretrained_model = self.load_pretrained_model()
        result = pretrained_model(self.image_input)
        print(result)
    
    