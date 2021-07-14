from django.urls import path
from . import views

urlpatterns = [
    # ex: /gallery/
    path('', views.all_art_pieces, name='gallery'),
    # ex: /gallery/5/
    path('<art_piece_id>', views.art_detail, name='art_detail'),
]
