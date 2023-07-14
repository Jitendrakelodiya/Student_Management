from django.urls import path
from .views import *
urlpatterns = [
    path("",Home),
    path("home/",Home,name="home"),
    path("std_add/",Student_add, name="std-add"),
    path("delete/<int:id>/",Student_delete, name="delete"),
    path("updates/<int:id>",Student_updates, name="updates"),
    path("updates_save/<int:id>",Student_updatesSave, name="updatessave"),
    
]