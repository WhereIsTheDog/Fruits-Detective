# -*- coding: utf-8 -*-
import base64 
import turicreate as tc
from urllib import parse

class ImageUtils:
    def __init__(self):
        pass

    @staticmethod
    def base64topicture(base64string):
        imgdata = base64.b64decode(base64string)
        # file = open('1.jpg','wb')
        # file.write(imgdata)
        # file.close()
        return imgdata
    
    @staticmethod
    def turi_predict(imagepath):
        label = ""
        model = tc.load_model("fruits_model")
        predict_data = tc.image_analysis.load_images(imagepath, with_path=True)
        predictions = model.predict(predict_data)
        label = str(predictions[0])
        return label
    
    @staticmethod
    def urlencoding(data):
        dataencodding = parse.unquote(data)
        return dataencodding