# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Obj(models.Model):
    name = models.CharField(u'名称', max_length=256)
    type = models.CharField(u'型号', max_length=256, default='no type')
    category = models.CharField(u'类别', max_length=256, default='no category')
    location = models.CharField(u'位置', max_length=256)
    buy_date = models.DateTimeField(u'购买时间', editable=True, default=datetime.now())
    buy_address = models.TextField(u'购买地点', max_length=2048, default='no address')
