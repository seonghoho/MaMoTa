from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('movie',)


class UserArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    like_users = LikeUserSerializer(read_only=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class Meta:
        model = Article
        fields = (
            'pk',
            'user',
            'movie',
            'title',
            'content',
            'rate',
            'like_users',
            'created_at',
            'updated_at',
            'like_user_count',
        )


# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk',)

    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'pk',
            'user',
            'movie',
            'content',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('movie',)
