from django.http import HttpResponse
from django.shortcuts import redirect, render

from projector.forms import CameraForm


class CameraCreateCommand:

    # TODO: create DIContainer to introduce object of Command and change class methods to instance methods

    @classmethod
    def execute(cls, request):
        if request.method == 'POST':
            return cls._save_camera(request)
        else:
            return cls._render_form(request, {'form': CameraForm()})

    @classmethod
    def _save_camera(cls, request) -> HttpResponse:
        form = CameraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cameras')
        else:
            return cls._render_form(request, {'form': form})

    @classmethod
    def _render_form(cls, request, context) -> HttpResponse:
        return render(request, 'projector/camera/camera_create.html', context)
