# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Inventory, Computer

# Index page just contains a list of inventories.
def index(request):
    inventories = Inventory.objects.all()
    context = { 'inventories': inventories }
    return render(request, 'inventory/index.html', context)

# Inventory page lists computers in a given inventory.
def inventory(request, inventory_id):
    # First get the associated inventory.
    try:
        name = Inventory.objects.get(pk=inventory_id).name
    except Inventory.DoesNotExist:
        raise Http404("Inventory does not exist")

    # Get and render the list of computers.
    computers = Computer.objects.filter(inventory=inventory_id)
    context = { 'name': name, 'computers': computers }
    return render(request, 'inventory/inventory.html', context)

# Returns form for adding a new inventory.
def add_inventory(request):
    if request.method == 'GET':
        return render(request, 'inventory/addinventory.html', {})
    elif request.method == 'POST':
        i = Inventory(name=request.POST['name'])
        i.save();
        return HttpResponseRedirect(reverse('inventory:index'))
