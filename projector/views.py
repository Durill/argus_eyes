from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views import generic

from projector.feed.feed_generator import generate_feed
from projector.models import Camera


def index(request):
    return HttpResponse("Projector index")


def camera_feed(request):
    print("camera feed")
    return render(request, 'projector/camera/camera_feed.html')


def video_feed(request):
    return StreamingHttpResponse(
        generate_feed(),
        content_type="multipart/x-mixed-replace; boundary=frame"
    )


class CameraListView(generic.ListView):
    model = Camera
    context_object_name = 'camera_list'
    queryset = Camera.objects.all()
    template_name = 'projector/camera/camera_list.html'


class CameraDeleteView(generic.DeleteView):
    model = Camera
    context_object_name = 'camera'
    success_url = '../'
    template_name = 'projector/camera/camera_delete.html'
