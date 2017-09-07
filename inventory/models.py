# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Basic inventory model
class Inventory(models.Model):
    name = models.CharField(max_length=256)

# Basic computer model
class Computer(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=256)
    serial = models.CharField(max_length=256)
    comments= models.CharField(max_length=1024)
