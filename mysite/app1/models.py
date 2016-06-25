# coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Obj(models.Model):
    name = models.CharField(u'名称', max_length=256)
    location = models.CharField(u'位置', max_length=256)
