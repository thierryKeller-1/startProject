from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import SolumadaUser as User
from .forms import UserRegistrationForm


class UserView(LoginRequiredMixin, TemplateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/admin/UserLists.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
        

class UserCreateView(CreateView, LoginRequiredMixin):
    model = User
    form_class = UserRegistrationForm
    login_url = reverse_lazy('login')
    template_name = 'users/admin/adminUser.html'
    success_url = reverse_lazy('userView')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    form_class = UserRegistrationForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserDeleteView(DeleteView, LoginRequiredMixin):
    model = User
    form_class = UserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    



