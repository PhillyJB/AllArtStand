from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from gallery.models import Art_Pieces


def bag_contents(request):

    bag_items = []
    total = 0
    art_count = 0
    bag = request.session.get('bag', {})

    for art_id, quantity in bag.items():
        art = get_object_or_404(Art_Pieces, pk=art_id)
        total += quantity * art.price
        art_count += quantity
        bag_items.append({
            'art_id': art_id,
            'quantity': quantity,
            'art': art,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'art_count': art_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
