from django.db import models
import os
from PIL import *


class Image(models.Model):
    filename = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.filename