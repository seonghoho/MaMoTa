from rest_framework import serializers
from movies.serializers import MovieListSerializer
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user',)


class ArticleListSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    movie = MovieListSerializer(read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users', )


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    movie = MovieListSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users')