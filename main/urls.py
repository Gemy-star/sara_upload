from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('video-upload', views.upload_video, name='video-upload'),
    path('show-videos', views.display, name='show-videos'),

]
