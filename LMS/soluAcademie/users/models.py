from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 

import uuid

class AccountManager(BaseUserManager):
    """class for object manager for users"""

    use_in_migrations = True

    def _create_student(self, email,name, mcode, numuser, typeuser, password, **extra_fields):
        values          = [email,name, mcode, numuser, typeuser]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        
        for field, value in field_value_map.items():
            if not value:
                raise ValueError(f"The value {field} is required")
        
        email = self.normalize_email(email)
        student  = self.model(
                            email=email,
                            name=name,
                            mcode=mcode,
                            numuser=numuser,
                            typeuser=typeuser
                        )
        student.set_password(password)
        student.save(using=self._db)
        return student

    def _create_teacher(self, email,name, mcode, numuser, typeuser, password, **extra_fields):
        values          = [email,name, mcode, numuser, typeuser]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        
        for field, value in field_value_map.items():
            if not value:
                raise ValueError(f"The value {field} is required")
        
        email = self.normalize_email(email)
        student  = self.model(
                                email=email,
                                name=name,
                                mcode=mcode,
                                numuser=numuser,
                                typeuser=typeuser
                            )
        student.set_password(password)
        student.save(using=self._db)
        return student
    
    def create_student(self, email, name, mcode, numuser, typeuser, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, mcode, numuser, typeuser, password, **extra_fields)


    def create_teacher(self, email, name, mcode, numuser, typeuser, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, mcode, numuser, typeuser, password, **extra_fields)


    def create_superuser(self, email, name, mcode, numuser, typeuser, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') != True and typeuser != 'admin':
            raise ValueError("superuser must have is_superuser=True")
        return self._create_user(email, name, mcode, numuser, typeuser, password, **extra_fields)


class SolumadaUser(AbstractBaseUser, PermissionsMixin):
    """Class for all type of user for Solumada Academie Users"""

    class TypeChoiceField(models.TextChoices):
        admin       = 'admin', _('admin')
        teacher     = 'teacher', ('teacher')
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
        ordering            = ["date_joined"]
        verbose_name_plural = "Users"
        permissions         =  [
                                    ("have_no_user_permissions", "Have No Permissions on User"),
                                    ("add_only", "Can Add User"),
                                    ("add_user_only", "Can Add User Only"),
                                    ("view_only", "Can Only View User"),
                                    ("add_update_view_only", "Can Add And View"),
                                    ("all_user_permissions", "Can Do everything to User"),
                                ]


    def __str__(self) -> str:
        super().__str__()
        return self.name


