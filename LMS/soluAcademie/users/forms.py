from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm

import re
from .models import SolumadaUser as User


class UserRegistrationForm(UserCreationForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'm_code', 'num_user', 'type_user', 'password', 'passwordConfirm')
    
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
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('passwordConfirm')

        if len(password1) > 8:
            raise forms.ValidationError("Password should be more than 8 chars")
        if not re.findall('[A-Z]', password1):
            raise forms.ValidationError("The password must contain at least 1 uppercase letter, A-Z")
        if not re.findall('[a-z]', password1):
            raise forms.ValidationError("The password must contain at least 1 lowercase letter a-z.")
        if not re.findall('\d', password1):
            raise forms.ValidationError("The password must contain at least 1 digit")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")

        return password1

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



