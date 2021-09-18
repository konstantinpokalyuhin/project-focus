from django.urls import path
from . import views

app_name = 'service_focus'

urlpatterns = [
    path('upload/', views.image_upload_view),
    path('', views.image_upload_view),
    path('result', views.number_pixels, name = 'pixels'),
] 