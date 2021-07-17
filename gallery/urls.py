from django.urls import path
from . import views

urlpatterns = [
    # ex: /gallery/
    path('', views.all_art_pieces, name='gallery'),
    # ex: /gallery/5/
    path('<int:art_piece_id>/', views.art_detail, name='art_detail'),
    path('add/', views.add_art, name='add_art'),
    path('edit/<int:art_piece_id>/', views.edit_art, name='edit_art'),
    path('delete/<int:art_piece_id>/', views.delete_art, name='delete_art'),
]
