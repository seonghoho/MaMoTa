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
    email = models.EmailField(unique=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    # email을 사용자 이름이자 unique한 값으로 설정해 회원가입 받음
    username = models.EmailField(unique=True)
    nickname = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(blank=False, null=False, max_length=255)    
    last_name = models.CharField(blank=False, null=False, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_pic = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)
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
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        
        # Remove this line: user_email(user, email)

        # user 객체를 다시 생성하지 않고 이미 생성된 객체를 사용
        user_username(user, username)
        # Instead, set the 'email' field directly
        user.email = email
        if password1:
            user_field(user, "password1", password1)
        if password2:
            user_field(user, "password2", password2)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
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