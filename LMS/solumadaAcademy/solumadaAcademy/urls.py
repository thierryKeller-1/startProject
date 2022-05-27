from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import BaseHomeView


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="log/login.html"), name='login'),
    path('solumadaAcademy.com/Home/', BaseHomeView.as_view(), name='home'),
    path('solumadaAcademy.com/Users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
