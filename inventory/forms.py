from django import forms

from .models import Brand, Camera, Drone


class DroneForm(forms.ModelForm):

    cameras = forms.ModelMultipleChoiceField(
        label="Compatible Camera's",
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        queryset=Camera.objects.all())

    class Meta:
        model = Drone
        exclude = ['added_date']


class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
