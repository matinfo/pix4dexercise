from django.conf.urls import url
from django.contrib.auth.decorators import permission_required

from .views import (
    DroneView,
    DroneAddView,
    DroneUpdateView,
    DroneDeleteView,
    CameraView,
    CameraAddView,
    CameraUpdateView,
    CameraDeleteView,
    BrandView,
    BrandUpdateView,
    BrandDeleteView,
)


urlpatterns = [
    url(r'^$',
        DroneView.as_view(),
        name="inventory-drone-list"),

    url(r'drone/add/$',
        permission_required('inventory.add_drone')(DroneAddView.as_view()),
        name="inventory-drone"),

    url(r'drone/(?P<pk>[0-9]+)/$',
        permission_required('inventory.change_drone')(DroneUpdateView.as_view()),
        name="inventory-drone-update"),

    url(r'drone/(?P<pk>[0-9]+)/delete/$',
        permission_required('inventory.delete_drone')(DroneDeleteView.as_view()),
        name="inventory-drone-delete"),

    url(r'^camera/$',
        CameraView.as_view(),
        name="inventory-camera-list"),

    url(r'camera/add/$',
        permission_required('inventory.add_camera')(CameraAddView.as_view()),
        name="inventory-camera"),

    url(r'camera/(?P<pk>[0-9]+)/$',
        permission_required('inventory.change_camera')(CameraUpdateView.as_view()),
        name="inventory-camera-update"),

    url(r'camera/(?P<pk>[0-9]+)/delete/$',
        permission_required('inventory.delete_camera')(CameraDeleteView.as_view()),
        name="inventory-drone-delete"),

    url(r'brand/$',
        permission_required('inventory.add_brand')(BrandView.as_view()),
        name="inventory-brand"),

    url(r'brand/(?P<pk>[0-9]+)/$',
        permission_required('inventory.change_brand')(BrandUpdateView.as_view()),
        name="inventory-brand-update"),

    url(r'brand/(?P<pk>[0-9]+)/delete/$',
        permission_required('inventory.delete_brand')(BrandDeleteView.as_view()),
        name="inventory-brand-delete"),
]
