from django.urls import path

from .views import UserView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('user/', UserView.as_view(), name='userView'),
    path('user/create/', UserCreateView.as_view(), name='userCreateView'),
    path('user/update/<uuid:pk>/', UserUpdateView.as_view(), name='userUpdateView'),
    path('users/delete/<uuid:pk>/', UserDeleteView.as_view(), name='userDeleteView'),
]
