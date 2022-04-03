from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserAccountCustomManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("Email Address is mandatory.")
        if not username:
            raise ValueError("Username is mandatory.")
        user = self.model(
            email=self.normalize_email(email),
            username = username, 
            first_name = first_name,
            last_name = last_name,
            )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name, 
            username = username,
            email = email, 
            password = password
            )
        user.is_admin = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user

# Create your models here.
class UserAccountCustomModel(AbstractBaseUser):
    id = models.UUIDField(default=uuid4(), primary_key=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(db_index=True, unique=True, null=False, blank=False)
    contact_number = models.CharField(max_length=20)

    # required fields: these fields are mandatory when craeting custom user model
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # tell this class to use custom acocunt manager instead of default user namager.
    object = UserAccountCustomManager()

    # changing default username field to email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'username', 'last_name')

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, object=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True