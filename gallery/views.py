from django.shortcuts import render, get_object_or_404
from .models import Art_Pieces


def all_art_pieces(request):
    """ A view to show all artwork, including sorting and serch queries"""

    # to return all art pieces from the db.:
    all_art = Art_Pieces.objects.all()
    # we add them to the context so are art pieces are available on template
    context = {
        'all_art': all_art,
    }

    return render(request, 'gallery/gallery.html', context)


def art_detail(request, art_piece_id):
    """ A view to show individual art pieces full details"""

    # to return all art pieces from the db.:
    art = get_object_or_404(Art_Pieces, pk=art_piece_id)
    # we add this to the context so are art
    # piece details are available on template
    context = {
        'art': art,
    }

    return render(request, 'gallery/art_detail.html', context)
