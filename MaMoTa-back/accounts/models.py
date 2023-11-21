from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# 이미지 썸네일 helper인 이미지킷 사용 
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        

        # Ensure that the 'email' parameter is provided
        email = self.normalize_email(email)

        # Use 'email' parameter instead of 'username' when calling create_user
        return self.create_user(username, email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    objects = UserManager()
    
    email = models.EmailField(unique=False)
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    username = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    REQUIRED_FIELDS  = ['email']
    
    def has_module_perms(self, app_label):
        return self.is_staff


class CustomAccountAdapter(DefaultAccountAdapter):
    
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field, user_username, user_email
        
        data = form.cleaned_data
        username = data.get("username")
        email = data.get("email")
        password1 = data.get("password1")
        password2 = data.get("password2")
        nickname = data.get("nickname")

        user_username(user, username)
        # user_email(user, email)
        if email:
            user_email(user, "email", email)
        if password1:
            user_field(user, "password1", password1)
        if password2:
            user_field(user, "password2", password2)
        if nickname:
            user_field(user, "nickname", nickname)
        if "password1" in data:
            user.set_password(raw_password=data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user