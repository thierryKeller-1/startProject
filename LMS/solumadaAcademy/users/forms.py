from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField

import re
from .models import SolumadaUser


class UserRegistrationForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = SolumadaUser
        fields = UserCreationForm.Meta.fields + ('email', 'username', 'm_code', 'num_user', 'type_user')
    
    def clean_name(self):
        username = self.cleaned_data.get('username')
        if User.objects.exists(username):
            raise forms.ValidationError("user with this username already exist")
        return username

    def clean_mcode(self):
        mcode = self.cleaned_data.get('m_code')
        if User.objects.exists('mcode'):
            raise forms.ValidationError("user with this M Code already exist")
        return mcode

    def clean_password(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2




    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        permissions = []
        if user.type_user == 'admin':
            user.is_superuser = True
            # user.User.user_permissions.set('all_user_permissions')
            user.save()
        else:
            # permissions.append('have_no_user_permissions')
            # user.user_permissions.set(permissions)
            user.save()
        return user


class UserUpdateForm(UserChangeForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = SolumadaUser
        fields = ('email', 'username', 'm_code', 'num_user', 'type_user')
    
    def clean_name(self):
        username = self.cleaned_data.get('username')
        if User.objects.exists(username):
            raise forms.ValidationError("user with this username already exist")
        return username

    def clean_mcode(self):
        mcode = self.cleaned_data.get('m_code')
        if User.objects.exists('mcode'):
            raise forms.ValidationError("user with this M Code already exist")
        return mcode

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        permissions = []
        if user.type_user == 'admin':
            user.is_superuser = True
            # user.User.user_permissions.set('all_user_permissions')
            user.save()
        else:
            # permissions.append('have_no_user_permissions')
            # user.user_permissions.set(permissions)
            user.save()
        return user



