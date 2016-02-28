import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Drone, Camera, Brand
from .forms import DroneForm, CameraForm, BrandForm


class DroneView(ListView):
    model = Drone
    template_name = 'inventory/drone_list.html'


class DroneAddView(SuccessMessageMixin, CreateView):
    template_name = 'inventory/drone_add_form.html'
    form_class = DroneForm
    success_url = reverse_lazy('inventory-drone-list')
    success_message = "Drone '%(model)s' was added successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            model=self.object.model,
        )

    def form_valid(self, form):
        return super(DroneAddView, self).form_valid(form)


class DroneUpdateView(SuccessMessageMixin, UpdateView):
    template_name_suffix = '_update_form'
    model = Drone
    form_class = DroneForm
    success_url = reverse_lazy('inventory-drone-list')
    success_message = "Drone '%(model)s' was updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            model=self.object.model,
        )

    def form_valid(self, form):
        return super(DroneUpdateView, self).form_valid(form)


class DroneDeleteView(DeleteView):
    model = Drone
    success_url = reverse_lazy('inventory-drone-list')
    success_message = "Drone '%(model)s' was deleted successfully"


class CameraView(ListView):
    model = Camera
    template_name = 'inventory/camera_list.html'


class CameraAddView(SuccessMessageMixin, CreateView):
    template_name = 'inventory/camera_add_form.html'
    form_class = CameraForm
    success_url = reverse_lazy('inventory-camera-list')
    success_message = "Camera '%(model)s' was added successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            model=self.object.model,
        )

    def form_valid(self, form):
        return super(CameraView, self).form_valid(form)


class CameraUpdateView(SuccessMessageMixin, UpdateView):
    template_name_suffix = '_update_form'
    model = Camera
    form_class = CameraForm
    success_url = reverse_lazy('inventory-camera-list')
    success_message = "Camera '%(model)s' was updated successfully"

    def get_context_data(self, **kwargs):
        context = super(CameraUpdateView, self).get_context_data(**kwargs)
        context['object_list'] = Camera.objects.all()
        return context

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            model=self.object.model,
        )

    def form_valid(self, form):
        return super(CameraUpdateView, self).form_valid(form)


class CameraDeleteView(DeleteView):
    model = Camera
    success_url = reverse_lazy('inventory-camera-list')
    success_message = "Camera '%(model)s' was deleted successfully"


class BrandView(SuccessMessageMixin, CreateView):
    template_name = 'inventory/brand.html'
    form_class = BrandForm
    success_url = reverse_lazy('inventory-brand')
    success_message = "Drone '%(name)s' was added successfully"

    def get_context_data(self, **kwargs):
        context = super(BrandView, self).get_context_data(**kwargs)
        context['object_list'] = Brand.objects.all()
        return context

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

    def form_valid(self, form):
        return super(BrandView, self).form_valid(form)


class BrandUpdateView(SuccessMessageMixin, UpdateView):
    template_name_suffix = '_update_form'
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('inventory-brand')
    success_message = "Brand '%(name)s' was updated successfully"

    def get_context_data(self, **kwargs):
        context = super(BrandUpdateView, self).get_context_data(**kwargs)
        context['object_list'] = Brand.objects.all()
        return context

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            model=self.object.name,
        )

    def form_valid(self, form):
        return super(BrandUpdateView, self).form_valid(form)


class BrandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy('inventory-brand')
    success_message = "Brand '%(model)s' was deleted successfully"
