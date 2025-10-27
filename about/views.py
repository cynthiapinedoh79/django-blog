from django.shortcuts import render

# Create your views here.

def about(request):
    """
    Renders the About page
    """
    return render(request, 'about.html')

