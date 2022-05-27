from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
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
        context['form'] = self.form_class
        return context

    def post(self):
        pass
        
# @login_required
def userlist(request):
    users = User.objects.all()
    data = [user.get_data() for user in users]
    response = {'data':data}
    return JsonResponse(response)

class UserCreateView(CreateView, LoginRequiredMixin):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/admin/adminUser.html"
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('userView')
    success_message = "User Created successfuly"
    
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


    



