from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from community.models import Article

# 로그인 커스터마이저
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
# 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255
    )
    first_name = serializers.CharField(
        required=True,
        max_length=255
    )    
    last_name = serializers.CharField(
        required=True,
        max_length=255
    )
    profile_pic = serializers.ImageField(
        max_length=None,  
        use_url=True,
        required=True,  
        allow_null=False,  
    )
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'email': self.validated_data.get('email', ''),

        }
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ArticleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title',)


# 영화 제목을 불러오기 위한 Serializer
class SimpleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path')


class ProfileSerializer(serializers.ModelSerializer):
    class FollowFollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'profile_pic')

    class ArticleSerializer(serializers.ModelSerializer):
        class LikeUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk',)

        like_users = LikeUserSerializer(read_only=True)
        like_user_count = serializers.IntegerField(
            source='like_users.count', read_only=True
        )
        movie = SimpleMovieSerializer(read_only=True)
        user = UserSerializer(read_only=True)

        class Meta:
            model = Article
            # exclude = ('user',)
            fields = '__all__'
            read_only_fields = ('movie',)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                'id',
                'title',
                'overview',
                'poster_path',
                'release_date',
                'like_users',
            )

    # like_articles = ArticleSerializer(many=True)
    followers = FollowFollowingSerializer(many=True, read_only=True)
    followings = FollowFollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(
        source='followers.count', read_only=True
    )
    following_count = serializers.IntegerField(
        source='followings.count', read_only=True
    )
    articles = ArticleSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    articles_count = serializers.IntegerField(
        source='articles.count', read_only=True
    )
    like_count = serializers.IntegerField(default=0)

    class Meta:
        model = User
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_pic')


class LikeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'user', 'like_users')
