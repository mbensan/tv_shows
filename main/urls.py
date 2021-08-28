from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('shows', views.shows),
    path('shows/<id>/edit', views.edit),
    path('shows/<id>/destroy', views.destroy),
    path('shows/create', views.create),
    path('shows/new', views.new_show),
    path('show', views.show),
]
