from django.forms import ModelForm

from projector.models import Camera


class CameraForm(ModelForm):
    class Meta:
        model = Camera
        fields = ('name', 'ip_address', 'suffix')
