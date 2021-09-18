from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import cv2
import numpy as np
from .forms import ImageForm
from .models import Image
import os
from focus.settings import MEDIA_ROOT

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj':img_obj,})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


def number_pixels(request):
    image =request.GET.get(os.path.join(str(MEDIA_ROOT), str(Image.filename)))
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    n_white_pix = np.sum(img == 255)
    n_black_pix = np.sum(img == 0)
    context = {
            'n_white_pix': n_white_pix,
            'n_black_pix': n_black_pix,
            }
    return render(request, context, 'result.html')