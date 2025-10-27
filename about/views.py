from django.shortcuts import render
from .models import About


def about_page(request):
    """
    View to display the About page
    """
    about = About.objects.first()
    return render(request, 'about/about.html', {'about': about})
