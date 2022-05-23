from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import SLMUser
from .forms import UserRegistrationForm


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = SLMUser
    form_class = UserRegistrationForm
    # template_name: str('addUser.html')

    def get_context_data(self, **kwargs):

        # adding list cours here

        context =  super().get_context_data(**kwargs)

        user = self.request.user

        return context
