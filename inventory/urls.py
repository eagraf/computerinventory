from django.conf.urls import url

from . import views

app_name = 'inventory'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<inventory_id>[0-9]+)/$', views.inventory, name='inventory'),
    url(r'^addinventory/$', views.add_inventory, name='addinventory'),
    url(r'^(?P<inventory_id>[0-9]+)/addcomputer/$', views.add_computer, name='addcomputer'),
    url(r'^(?P<inventory_id>[0-9]+)/editcomputer/(?P<computer_id>[0-9]+)/$', views.edit_computer, name='editcomputer'),
]
