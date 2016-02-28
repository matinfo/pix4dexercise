from django.contrib import admin

from .models import Brand, Camera, Drone


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'megapixel',)
    search_fields = ('model', 'brand__name',)
    list_filter = ('megapixel',)


class CameraInline(admin.TabularInline):
    model = Drone.cameras.through


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'serial_number',)
    list_filter = ('cameras',)
    search_fields = ('model', 'brand__name', 'serial_number',)
    inlines = (CameraInline,)
    exclude = ('cameras',)
