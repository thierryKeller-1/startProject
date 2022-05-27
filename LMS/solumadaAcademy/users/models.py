from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 

import uuid

from .manager import AccountManager


class SolumadaUser(AbstractBaseUser, PermissionsMixin):
    """Class for all type of user for Solumada Academie Users"""

    class TypeChoiceField(models.TextChoices):
        admin       = 'admin', _('admin')
        teacher     = 'teacher', _('teacher')
        participant = 'participant', _('participant')
    
    user_id = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="user email", unique=True, blank=False)
    username = models.CharField(max_length=50, verbose_name='username', blank=False)
    m_code = models.CharField(max_length=50, verbose_name="M Code", blank=False)
    num_user = models.CharField(max_length=50, verbose_name="Num Agent", blank=False)
    type_user = models.CharField(max_length=50, choices=TypeChoiceField.choices, default=TypeChoiceField.participant, verbose_name='type user', blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    # picture = models.ImageField()
    objects     = AccountManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','m_code', 'num_user', 'type_user']

    class Meta:
        ordering            = ["-date_joined"]
        verbose_name_plural = "SolumadaUsers"
        permissions         =  [
                                    ("have_no_user_permissions", "Have No Permissions on User"),
                                    ("all_user_permissions", "Can Do everything to User"),
                                ]


    def __str__(self) -> str:
        super().__str__()
        return self.email


