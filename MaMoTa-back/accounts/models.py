from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# 이미지 썸네일 helper인 이미지킷 사용 
# 
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model


from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user.email:  
            user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

from django.urls import reverse

class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    # email을 사용자 이름이자 unique한 값으로 설정해 회원가입 받음
    username = models.EmailField(unique=True)
    email = models.EmailField(null=True)
    nickname = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(blank=False, max_length=255)    
    last_name = models.CharField(blank=False, max_length=255)
    
    # 원본 이미지를 재가공해서 저장함
    profile_pic = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
	)



class CustomAccountAdapter(DefaultAccountAdapter):
    
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        
        
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        
        # user 객체를 다시 생성하지 않고 이미 생성된 객체를 사용
        user_email(user, email)
        user_username(user, username)
        
        if email:
            user_email(user, email)
        if username:
            user_username(user, username)
        
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