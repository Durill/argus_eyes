from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from projector.forms import CameraForm
from projector.models import Camera


class CameraUpdateCommand:

    # TODO: create DIContainer to introduce object of Command and change class methods to instance methods

    @classmethod
    def execute(cls, request: WSGIRequest, id: int):
        camera = get_object_or_404(Camera, pk=id)

        if request.method == 'POST':
            return cls._update_camera(camera, request)
        else:
            form = cls._fill_out_form(camera)
            return cls._render_form(request, {'form': form})

    @classmethod
    def _update_camera(cls, camera: Camera, request) -> HttpResponse:
        form = CameraForm(request.POST)

        if form.is_valid():
            cls._update_camera_object(camera, **form.cleaned_data)
            camera.save()
            return redirect('cameras')
        else:
            return cls._render_form(request, {'form': form})

    @classmethod
    def _update_camera_object(cls, camera: Camera, name: str, ip_address: str, suffix: str):
        camera.name = name
        camera.ip_address = ip_address
        camera.suffix = suffix

        return camera

    @classmethod
    def _render_form(cls, request, context) -> HttpResponse:
        return render(request, 'projector/camera/camera_edit.html', context)

    @classmethod
    def _fill_out_form(cls, camera: Camera) -> CameraForm:
        return CameraForm(
            initial={
                'name': camera.name,
                'ip_address': camera.ip_address,
                'suffix': camera.suffix,
            }
        )
