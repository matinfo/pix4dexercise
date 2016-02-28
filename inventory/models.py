from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Brand(models.Model):
    """Brand of drone or camera"""
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return '{0}'.format(self.name)

    def get_absolute_url(self):
        return reverse('inventory-brand-update', kwargs={'pk': self.pk})

    def num_linked(self):
        return self.drones.count() + self.cameras.count()


class Camera(models.Model):
    """Camera for drone"""
    model = models.CharField(max_length=200, unique=True)
    brand = models.ForeignKey(Brand, related_name='cameras', null=True)
    megapixel = models.FloatField()

    def __unicode__(self):
        return '{0} - {1}'.format(self.model, self.brand)

    def get_absolute_url(self):
        return reverse('inventory-camera-update', kwargs={'pk': self.pk})

    def num_of_drone(self):
        return self.drones.count()


class Drone(models.Model):
    """Drone registered"""
    model = models.CharField(max_length=200, unique=True)
    brand = models.ForeignKey(Brand, related_name='drones', null=True)
    serial_number = models.CharField(max_length=20)
    added_date = models.DateTimeField('date added', default=timezone.now)
    cameras = models.ManyToManyField(Camera, related_name='drones', blank=True)

    class Meta:
        ordering = ['brand']

    def __unicode__(self):
        return '{0} - {1}'.format(self.model, self.brand)

    def get_absolute_url(self):
        return reverse('inventory-drone-update', kwargs={'pk': self.pk})
