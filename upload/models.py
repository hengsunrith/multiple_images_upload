# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import os
import uuid


def get_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images', filename)

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)


class Images(models.Model):
    post = models.ForeignKey(Post, default=None)
    image = models.ImageField(upload_to=get_file_name, verbose_name='Image')