from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

# 영화 리스트
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'vote_average', 'vote_count', 'poster_path')


class TopMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = (
            'popularity',
            'tagline',
            'words',
            'budget',
            'revenue',
            'runtime',
        )


# 단일 영화 상세 정보
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name', 'profile_path')

    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)
    like_movies = UserSerializer(read_only=True, many=True)
    
    class Meta:
        model = Movie
        exclude = (
            'popularity',
            'tagline',
            'vote_count',
            'words',
            'like_users',
        )


# 날씨 기반 추천 장르 영화
class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'release_date')



# 명대사
class FamousLineSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    user = UserSerializer(read_only=True)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            # fields = ('pk', 'username', 'profile_pic')
            fields = ('pk',)

    class Meta:
        model = FamousLine
        fields = (
            'pk',
            'user',
            'movie',
            'content',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('user','movie',)



# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            # fields = ('pk', 'username', 'profile_pic')
            fields = ('pk',)

    user = UserSerializer(read_only=True)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk',)

    class Meta:
        model = Review
        fields = (
            'pk',
            'user',
            'movie',
            'content',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('movie',)
