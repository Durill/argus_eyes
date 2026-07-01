from django.db import models
from django.forms import ModelForm


class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField()
    suffix = models.CharField(max_length=100, default='')


class CreateCameraForm(ModelForm):
    class Meta:
        model = Camera
        fields = ('name', 'ip_address', 'suffix')


class EditCameraForm(ModelForm):
    class Meta:
        model = Camera
        fields = ('name', 'ip_address', 'suffix')
