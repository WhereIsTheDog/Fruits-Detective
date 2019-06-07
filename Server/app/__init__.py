#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['MONGODB_SETTINGS'] = {
    'db':   'nickfu',
    'host': '127.0.0.1',
    'port': 27017
}

db = MongoEngine(app)

#数据库对应的模型
#import models

#api的业务逻辑
import controllers