from django.urls import path
from . import views

app_name = 'collaboration'

urlpatterns = [
    path('', views.collaboration_request, name='request'),
]
