from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('comment/<int:comment_id>/approve/', views.approve_comment, name='approve_comment'),
    path('comment/<int:comment_id>/disapprove/', views.disapprove_comment, name='disapprove_comment'),
]
