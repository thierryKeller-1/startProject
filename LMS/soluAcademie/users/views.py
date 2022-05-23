from pyexpat import model
from typing import Any, Dict
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


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        

        context =  super().get_context_data(**kwargs)

        return context
