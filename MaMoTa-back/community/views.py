from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleListSerializer, CommentSerializer, ArticleSerializer
from .models import Article, Comment
from movies.models import Movie
from accounts.serializers import ProfileSerializer


# 게시글 전체 조회
@api_view(['GET'])
def article_list(request):
    article = Article.objects.order_by('-pk')
    context = {
        'article': ArticleListSerializer(article, many=True).data,
    }
    return Response(context)


# 게시글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


# 게시글 디테일페이지, 수정, 삭제
@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        
        if article.like_users.filter(pk=request.user.pk).exists():
            is_liked = True
        else:
            is_liked = False
        context = {
            'data': serializer.data,
            'is_liked': is_liked,
        }
        return Response(context)
    
    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        if request.user == article.user:
            serializer = ArticleListSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)



# 게시글 좋아요 
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        is_liked = False
    
    else:
        article.like_users.add(request.user)
        is_liked = True
        
    context = {
        'is_liked': is_liked,
        'like_count' : article.like_users.count()
    }

    return Response(context)



# 댓글 리스트
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    
# 댓글 생성
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 삭제
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def comment_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = article.comment_set.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
