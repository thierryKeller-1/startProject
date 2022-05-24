from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import User
from .forms import UserRegistrationForm


class UserView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    model = User
    form_class = UserRegistrationForm
    permissions =  {
                        "all": ('user.all_user_permissions'),
                        "any": ('view_only', 'add_update_view_only'),
                    }
    permission_denied_message = f"User view is only allow for admin"

    # login_url = reverse_lazy('login')
    # template_name: str('adminUser.html')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class UserCreateView(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = User
    permissions =  {
                        "all": ('user.all_user_permissions'),
                        "any" : ('user.add_only', 'add_update_view_only'),
                    }
    # login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context


class UserUpdateView(UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = User
    permissions =  {
                        "all": ('user.all_user_permissions'),
                        "any" : ('user.add_only', 'add_update_view_only'),
                    }
    # login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context


class UserDeleteView(DeleteView, PermissionRequiredMixin, LoginRequiredMixin):
    model = User
    permissions =  {
                        "all": ('user.all_user_permissions')
                    }
    # login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context
    



