from django.contrib import admin
from .models import SolumadaUser as soluUser
from django.contrib.auth.models import Group


# admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(soluUser)
class Adminuser(admin.ModelAdmin):
    list_display = ['pk', 'email', 'username', 'm_code', 'num_user', 'type_user', 'date_joined']
    list_filter = ['email', 'username', 'm_code', 'num_user', 'type_user', 'date_joined']


