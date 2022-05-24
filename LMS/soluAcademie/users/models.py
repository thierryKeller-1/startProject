from email.mime.image import MIMEImage
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class AccountManager(BaseUserManager):
    """class object manager for users"""

    use_in_migrations = True

    def _create_user(self, email,name, mcode, numuser, typeuser, password, **extra_fields):
        values          = [email,name, mcode, numuser, typeuser]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        
        for field, value in field_value_map.items():
            if not value:
                raise ValueError(f"The value {field} is required")
        
        email = self.normalize_email(email)
        user  = self.model(
                            email=email,
                            name=name,
                            mcode=mcode,
                            numuser=numuser,
                            typeuser=typeuser
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, name, mcode, numuser, typeuser, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, mcode, numuser, typeuser, password, **extra_fields)

    def create_superuser(self, email, name, mcode, numuser, typeuser, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True and typeuser not 'admin':
            raise ValueError("superuser must have is_superuser=True")
        return self._create_user(email, name, mcode, numuser, typeuser, password, **extra_fields)


class SLMUser(AbstractBaseUser, PermissionsMixin):
    """Class for all type of user for Solumada Academie Users"""

    class TypeChoiceField(models.TextChoices):
        admin       = 'admin', _('admin')
        teacher     = 'teacher', ('teacher')
        participant = 'participant', _('participant')

<<<<<<< HEAD
    email        = models.EmailField(verbose_name="user email")
    name         = models.CharField(max_length=50, verbose_name='username')
    mcode        = models.CharField(max_length=50, verbose_name="M Code")
    numuser      = models.CharField(max_length=50, verbose_name="Num Agent")
    typeuser     = models.CharField(max_length=50, choices=TypeChoiceField.choices, default=TypeChoiceField.participant)
    is_staff     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    date_joined  = models.DateTimeField(default=timezone.now)
    date_created = models.DateFieldTimeField(auto_now=True) 
    date_updated = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
=======
    email = models.EmailField(verbose_name="user email", unique=True)
    username = models.CharField(max_length=50, verbose_name='username')
    mcode = models.CharField(max_length=50, verbose_name="M Code")
    numuser = models.CharField(max_length=50, verbose_name="Num Agent")
    typeuser = models.CharField(max_length=50, choices=TypeChoiceField.choices, default=TypeChoiceField.participant, verbose_name='type user')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
>>>>>>> e384a9502dfb9ebb7dd5ee5dc38cf5a65b454a4f
    # picture = models.ImageField()
    objects     = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','mcode', 'numuser', 'typeuser']

    class Meta:
        ordering = ["date_joined"]
        verbose_name_plural = "SLMUsers"
        permissions = ['add_user', 'change_user', 'delete_user', 'add_only', 'all']


    def __str__(self) -> str:
        super().__str__()
        return self.name

