#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db
from models.device import Device1

# 类名定义 collection
class Image(db.Document):
    # 字段
    time = db.StringField()
    picture = db.StringField()
    # env = db.StringField(required=False, max_length=50)
    label = db.StringField(required=False)
    # device = db.ReferenceField(Device1)
    # devices = db.ListField(db.ReferenceField(Device1))
    # emdevices = db.ListField(db.EmbeddedDocumentField("Device1"))

    def __str__(self):
        return "picture:{} - phone:{}".format(self.picture, self.label)

