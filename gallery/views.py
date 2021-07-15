from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Art_Pieces


def all_art_pieces(request):
    """ A view to show all artwork, including sorting and search queries"""

    # to return all art pieces from the db.:
    all_art = Art_Pieces.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                all_art = all_art.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            all_art = all_art.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didnt enter any search criteria!")
                return redirect(reverse('gallery'))

            # TODO: This is a hack. Lookups with Q objects are probably not
            # ideal for seacrhing based on category due to the
            # unfrienedly category name i.e. PPLE etc.
            # for examples on what Q objects permit check out.
            # https://github.com/django/django/blob/main/tests/or_lookups/
            # tests.py
            # Filtering on category based on a checkbox is a better approach
            # Suggestion to refactor this: place the query translation code
            # outside of view. View shouldn't do "real" work, just handling and
            # returnig http

            if query.lower() == "people":
                query = Art_Pieces.PEOPLE
            elif query.lower() == "animal":
                query = Art_Pieces.ANIMAL
            elif query.lower() == "location":
                query = Art_Pieces.LOCATIONS
            elif query.lower() == "objects":
                query = Art_Pieces.OBJECTS
            elif query.lower() == "building":
                query = Art_Pieces.BUILDINGS

            queries = Q(title__icontains=query) | Q(category__icontains=query)
            all_art = all_art.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # we add them to the context so are art pieces are available on template
    context = {
        'all_art': all_art,
        'search_art': query,
        'current_sorting': current_sorting,
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
