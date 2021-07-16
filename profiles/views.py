from django.shortcuts import render


def profile(request):
    """ Display the user's profile. """
    template = 'profiles/profile.html'
    contxet = {}

    return render(request, template, contxet)
