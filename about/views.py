from django.shortcuts import render
from .models import About


def about_page(request):
    """
    View to display the About page.
    Retrieves the first About object. If multiple exist, only the first is shown.
    If none exist, the template will display a message prompting admin to add content.
    """
    about = About.objects.first()
    return render(request, 'about/about.html', {'about': about})
