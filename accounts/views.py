from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserRegistrationForm


class RegisterView(generic.CreateView):
    """View for user registration"""
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Log the user in after registration
        login(self.request, self.object)
        messages.success(self.request, 'Registration successful! Welcome to the blog.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

