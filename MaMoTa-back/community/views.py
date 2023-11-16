from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import (ArticleSerializer, UserArticleSerializer)

from .models import Movie, Article, Comment


# article 조회, 생성
@api_view(['GET', 'POST'])
def article_list_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    def article_list():
        articles = (
            Article.objects.filter(movie_id=movie_pk)
            .annotate(likes_count=Count('like_users'))
            .order_by('-likes_count')
        )
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        return create_article()
    elif request.method == 'GET':
        return article_list()


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def articles_get_or_update_or_delete(request, movie_pk, article_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    article = get_object_or_404(Article, pk=article_pk)

    def update_rating():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                articles = movie.articles.all()
                serializer = ArticleSerializer(articles, many=True)
                return Response(serializer.data)

    def delete_rating():
        if request.user == article.user:
            article.delete()
            articles = movie.articles.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

    def get_article():
        serializer = UserArticleSerializer(article)
        return Response(serializer.data)

    def like_article():
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        else:
            article.like_users.add(user)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

    if request.method == 'PUT':
        return update_rating()
    elif request.method == 'DELETE':
        return delete_rating()
    elif request.method == 'GET':
        return get_article()
    elif request.method == 'POST':
        return like_article()


@api_view(['GET', 'POST'])
def get_create_comment(request, movie_pk, article_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=user)
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_comment(request, movie_pk, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request, movie_pk, article_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.like_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
