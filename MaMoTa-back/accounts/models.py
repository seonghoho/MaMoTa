from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# 이미지 썸네일 helper인 이미지킷 사용 
# 
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # email을 사용자 이름이자 unique한 값으로 설정해 회원가입 받음
    username = models.EmailField(unique=True)
    
    # 원본 이미지를 재가공해서 저장함
    profile_pic = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)