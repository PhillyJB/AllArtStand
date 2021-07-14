from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_art_pieces, name='gallery'),
]
