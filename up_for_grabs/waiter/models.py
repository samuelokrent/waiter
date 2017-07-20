# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Order(models.Model):
    description = models.CharField(max_length=512)
    owner_name = models.CharField(max_length=200)
    office = models.CharField(max_length=32)
    arrival_time = models.TimeField('Arrival Time')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('order_edit', kwargs={'pk': self.pk})