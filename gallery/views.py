from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Art_Pieces
from .forms import Art_PiecesForm


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


@login_required
def add_art(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = Art_PiecesForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save()
            messages.success(request, 'Successfully added art piece!')
            return redirect(reverse('art_detail', args=[art.id]))
        else:
            messages.error(
                request, 'Failed to add art piece. Please ensure the form is valid.')
    else:
        form = Art_PiecesForm()

    template = 'gallery/add_art.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_art(request, art_piece_id):
    """Edit art piece in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    art_piece = get_object_or_404(Art_Pieces, pk=art_piece_id)
    if request.method == 'POST':
        form = Art_PiecesForm(request.POST, request.FILES, instance=art_piece)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated art piece!')
            return redirect(reverse('art_detail', args=[art_piece.id]))
        else:
            messages.error(request, 'Failed to update art piece. Please ensure the form is valid.')
    else:
        form = Art_PiecesForm(instance=art_piece)
        messages.info(request, f'You are editing {art_piece.name}')

    template = 'gallery/edit_art.html'
    context = {
        'form': form,
        'art_piece': art_piece,
    }

    return render(request, template, context)


@login_required
def delete_art(request, art_piece_id):
    """ Delete an art pieve from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    art_piece = get_object_or_404(Art_Pieces, pk=art_piece_id)
    art_piece.delete()
    messages.success(request, 'Art piece deleted!')
    return redirect(reverse('gallery'))
