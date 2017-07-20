# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food_edit', kwargs={'pk': self.pk})