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
    # Render form if GET is used.
    if request.method == 'GET':
        return render(request, 'inventory/addinventory.html', {})
    # Add a new inventory if POST is used.
    elif request.method == 'POST':
        inventory = Inventory(name=request.POST['name'])
        inventory.save();
        return HttpResponseRedirect(reverse('inventory:index'))

# Form for adding a new computer to a inventory.
def add_computer(request, inventory_id):
    # First get the inventory (necessary for both get and post).
    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except Inventory.DoesNotExist:
        raise Http404("Inventory does not exist")

    # Render the form if GET is used
    if request.method == 'GET':
        context = { 'inventory': inventory }
        return render(request, 'inventory/addcomputer.html', context)
    # Add new computer to an inventory if POST is used
    elif request.method == 'POST':
        # Create the computer in the correct inventory.
        computer = Computer(serial=request.POST['serial'], manufacturer=request.POST['manufacturer'], comments=request.POST['comments'], inventory=inventory)
        computer.save()
        return HttpResponseRedirect(reverse('inventory:inventory', args=(inventory_id,)))
