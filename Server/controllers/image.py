#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from flask import Flask, jsonify, request, abort
from datetime import datetime
from models.image import Image
from models.device import Device1
from utils.image_utils import ImageUtils
# import os

@app.route('/todo/api/v1/image', methods=['GET'])
def get_image():
    if (request.args.get('time')==""):
        print(request)
        abort(400)

    image = Image.objects(time=request.args.get('time')).first()

    # print(image.picture)
    pic = ImageUtils.base64topicture(image.picture)
    file = open('/search/pic.jpg','wb')
    file.write(pic)
    file.close

    perdict = ImageUtils.turi_predict('search/pic.jpg')
    image.label = perdict
    
         #判断文件是否存在
    # if(os.path.exists("search/pic.jpg")):
    #     os.remove("search/pic.jpg")

    # return jsonify({'imageinfo': image}),200
    
    return jsonify({'imageinfo': perdict}),200

@app.route('/todo/api/v1/image', methods=['POST'])
def create_image():
    if (request.args.get('time')=="" or request.args.get('picture')==""):
        print(request)
        abort(400)

    print(request.args.get('picture'))
    # picturedata = request.args.get('picture')
    # picturedata = ImageUtils.urlencoding(picturedata)
    
    Image(time = request.args.get('time'),picture = ImageUtils.urlencoding(request.args.get('picture'))).save()

    # return jsonify({'imageinfo': Image.objects.all()}), 201

    # return ("Ok"), 200
    image = Image.objects(time=request.args.get('time')).first()
    # print(image.picture)
    return jsonify({'imageinfo': image}),200