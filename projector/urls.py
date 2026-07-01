from django.urls import path

from . import views
from .camera import CameraCreateCommand, CameraUpdateCommand
from .views import CameraDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('cameras/feed', views.camera_feed, name='camera_feed'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('cameras/', views.CameraListView.as_view(), name='cameras'),
    path('cameras/create/', CameraCreateCommand.execute, name='create_camera'),
    path('cameras/<int:id>/edit', CameraUpdateCommand.execute, name='edit_camera'),
    path('cameras/<pk>/delete', CameraDeleteView.as_view(), name='delete_camera'),
]
