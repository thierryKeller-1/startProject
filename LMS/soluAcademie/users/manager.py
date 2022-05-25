from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AccountManager(BaseUserManager):
    """class for object manager for users"""

    use_in_migrations = True

    def _create_user(self, email, username, m_code, num_user, type_user, password, **extra_fields):
        values          = [email, username, m_code, num_user, type_user]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        
        for field, value in field_value_map.items():
            if not value:
                raise ValueError(f"The value {field} is required")
        
        email = self.normalize_email(email)
        user  = self.model(
                            email=email,
                            username=username,
                            m_code=m_code,
                            num_user=num_user,
                            type_user=type_user,
                            **extra_fields
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, m_code, num_user, type_user, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, m_code, num_user, type_user, password, **extra_fields)

    def create_superuser(self, email, username, m_code, num_user, type_user, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_superuser'] = True
        if extra_fields.get('is_superuser') != True and extra_fields.get('is_superuser') != True:
            raise ValueError("superuser must have is_superuser=True")
        return self._create_user(email, username, m_code, num_user, type_user, password, **extra_fields)