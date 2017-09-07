# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Index page just contains a list of inventories.
def index(request):
    return HttpResponse("Index")

# Inventory page lists computers in a given inventory.
def inventory(request, inventory_id):
    return HttpResponse("Inventory")
