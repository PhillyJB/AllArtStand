from django.shortcuts import render
from .models import Art_Pieces
# Create your views here.


def all_art_pieces(request):
    """ A view to show all artwork, including sorting and serch queries"""

    # to return all art pieces from the db.:
    all_art = Art_Pieces.objects.all()
    # we add them to the context so are art pieces are available on template
    context = {
        'all_art': all_art,
    }

    return render(request, 'gallery/gallery.html', context)
