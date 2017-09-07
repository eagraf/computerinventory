# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Inventory, Computer

# Index page just contains a list of inventories.
def index(request):
    inventories = Inventory.objects.all()
    context = { 'inventories': inventories }
    return render(request, 'inventory/index.html', context)

# Inventory page lists computers in a given inventory.
def inventory(request, inventory_id):
    name = Inventory.objects.get(pk=inventory_id).name
    computers = Computer.objects.filter(inventory=inventory_id)
    context = { 'name': name, 'computers': computers }
    return render(request, 'inventory/inventory.html', context)
