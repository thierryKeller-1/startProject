from django.urls import path

from .views import UserView, UserCreateView, UserUpdateView, UserDeleteView
from . import views
urlpatterns = [
    path('', UserView.as_view(), name='userView'),
    path('lists/', views.userlist, name='userListView'),
    path('create/', UserCreateView.as_view(), name='userCreateView'),
    path('update/<uuid:pk>/', UserUpdateView.as_view(), name='userUpdateView'),
    path('delete/<uuid:pk>/', UserDeleteView.as_view(), name='userDeleteView'),
]
