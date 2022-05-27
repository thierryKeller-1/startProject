from django.urls import path

from .views import UserView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('lists/', UserView.as_view(), name='userView'),
    path('create/', UserCreateView.as_view(), name='userCreateView'),
    path('update/<uuid:pk>/', UserUpdateView.as_view(), name='userUpdateView'),
    path('delete/<uuid:pk>/', UserDeleteView.as_view(), name='userDeleteView'),
]
