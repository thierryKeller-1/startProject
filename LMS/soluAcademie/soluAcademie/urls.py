from django.contrib import admin
from django.urls import path, include
# from .views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.login),
    # path('', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
