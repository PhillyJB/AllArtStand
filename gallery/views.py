from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Art_Pieces


def all_art_pieces(request):
    """ A view to show all artwork, including sorting and serch queries"""

    # to return all art pieces from the db.:
    all_art = Art_Pieces.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didnt enter any search criteria!")
                return redirect(reverse('gallery'))

            queries = Q(title__icontains=query) | Q(category__icontains=query)
            all_art = all_art.filter(queries)

    # we add them to the context so are art pieces are available on template
    context = {
        'all_art': all_art,
        'search_art': query,
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
