from django.contrib import admin
from .models import SolumadaUser 
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


from .forms import UserRegistrationForm, UserUpdateForm

# admin.site.unregister(User)
# admin.site.unregister(Group)
class SolumadaUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserUpdateForm

    list_display = ['pk', 'email', 'username', 'm_code', 'num_user', 'type_user', 'date_joined']
    list_filter = ['email', 'username', 'm_code', 'num_user', 'type_user', 'date_joined']


admin.site.register(SolumadaUser, SolumadaUserAdmin)


