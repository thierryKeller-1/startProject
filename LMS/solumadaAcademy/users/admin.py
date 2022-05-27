from django.contrib import admin
from .models import SolumadaUser 
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import SolumadaUser
from .forms import UserRegistrationForm, UserUpdateForm

# admin.site.unregister(User)
# admin.site.unregister(Group)
class SolumadaUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserUpdateForm
    model = SolumadaUser

    fieldsets = UserAdmin.fieldsets + (
         (None, { 'fields': ('m_code', 'num_user', 'type_user')}),
    )

    add_fiedsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('m_code', 'num_user', 'type_user')
            }
        ),
    )

    list_display = ['email', 'username', 'm_code', 'num_user', 'type_user', 'date_joined']
    list_filter = ['email', 'username', 'm_code', 'num_user', 'type_user', 'date_joined']

    search_fields = ['email']


admin.site.register(SolumadaUser, SolumadaUserAdmin)


